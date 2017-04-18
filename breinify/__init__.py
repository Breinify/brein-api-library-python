import base64
import copy
import hashlib
import hmac
import json
import logging
import requests
import time
from multiprocessing import Pool

from . import brein_exception
from . import validFields


class User:
    """
    A specific user on your site
    """

    def __init__(self, **kwargs):
        """
        Potential identifiers for the user. All fields are optional, but additional identifiers may improve the
        accuracy of the results.
        :param email: The user's email
        :param firstname: The user's first name
        :param lastname: The user's last name
        :param dateofbirth: The user's date of birth (MM/DD/YYYY)
        :param imei: A user's cellular device
        :param deviceid: A user's device's unique identifier
        :param sessionid: A web session ID
        :param ip: A user's ip address
        :param agentstring: A user's web browser's user agent string
        :param location: A map of (longitude+latitude)
        :param localDateTime: The user's local time
        :param timeZone: the user's timezone
        """
        validUserFields = ["email",
                           "firstname",
                           "lastName",
                           "dateofbirth",
                           "imei",
                           "deviceid",
                           "sessionid",
                           "ip",
                           "agentstring",
                           "location",
                           "localDateTime",
                           "timeZone"]

        for param in validUserFields:
            if kwargs.get(param) is not None:
                self.__dict__[param] = kwargs.get(param)


class Breinify:
    def __init__(self, api_key, secret=None, service_end_point="https://api.breinify.com/", threadPoolSize=10):
        """Initialize a connection to the Breinify API
        :param api_key: Your API key, available through Breinify.com
        :param secret: Your (optional) secret key to sign calls to the Breinify API
        :param service_end_point: for debugging purposes
        :param threadPoolSize: The number of threads to handle asynchronous activity pushes
        """
        self.api_key = api_key
        self.service_end_point = service_end_point
        self.pool = Pool(processes=threadPoolSize)
        self.secret = secret

    def send_activity(self,
                      user,
                      activity_type,
                      category=None,
                      description=None,
                      tags=None,
                      url=None,
                      referrer=None,
                      activity_time=None):
        """
        Reports a user's activity to the Brein Engine
        :param user: The user who's activity is being reported
        :param activity_type: The type of activity
        :param category: The category of the activity
        :param description: A free text description of the activity
        :param tags: Custom tags describing the activity
        :param url: A description of where the activity took place
        :param referrer: Where the user came from
        :param activity_time: A unix timestamp of when the activity happened
        """
        userResult = copy.copy(user.__dict__)

        to_push = {"apiKey": self.api_key}

        additional = {}

        if url is not None:
            additional['url'] = url

        if referrer is not None:
            additional['referrer'] = referrer

        if 'agentString' in userResult:
            additional['userAgent'] = userResult['agentstring']
            del userResult['agentstring']

        if 'ip' in userResult:
            to_push['ipAddress'] = userResult['ip']
            del userResult['ip']

        if len(additional) > 0:
            userResult['additional'] = additional

        to_push['user'] = userResult

        if activity_time is None:
            to_push['unixTimestamp'] = round(time.time())
        else:
            to_push['unixTimestamp'] = activity_time

        activity = {"type": activity_type,
                    "category": category,
                    "description": description}

        if tags is not None:
            activity['tags'] = tags

        to_push['activity'] = activity
        return self.pool.apply_async(self.__pushActivity__, (to_push,))

    def lookup(self, user, dimensions):
        """
        Lookup a given user's information
        :param user: The user that you want data about
        :param dimensions: What types of data do you want?
        :                  (see getSupportedLookupDimensions())
        :param sign: Should we sign this lookup with your secret key?
        :return: A map containing information about each of the specified
        :        dimensions for the user
        """
        to_push = {"user": user.__dict__, "lookup": {"dimensions": dimensions},
                  "apiKey": self.api_key, "unixTimestamp": round(time.time())}
        for dim in dimensions:
            if not dim in self.getSupportedLookupDimensions():
                raise brein_exception.invalidArgumentException(dim,self.getSupportedLookupDimensions())
        if self.secret is not None:
            self.__signLookup(to_push)
        response = requests.post(self.service_end_point + "lookup",
                                 data=json.dumps(to_push))
        if response.status_code != 200:
            raise brein_exception.BreinAPIConnectionError(response)
        result = json.loads(response.text)
        return result

    def temporal_data(self,
                      user=None,
                      unixtime=None,
                      ip=None,
                      location_free_text=None,
                      location_city=None,
                      location_state=None,
                      location_country=None,
                      location_latitude=None,
                      location_longitude=None,
                      location_shapes=None):
        """
        Looks up information about a given location at a given time
        :param user: The user info to be used to resolve the location
        :param unixtime: The time for which data should be looked up for
        :param ip: An ip address to resolve
        :param location_free_text: A free text field to resolve a location from,
                                   example values are "San Francisco, CA" or "NYC"
        :param location_city: The name of the city you want to resolve
        :param location_state: The name of the state you want to resolve
        :param location_country: The name of the country you want to resolve
        :param location_latitude: The latitude to resolve, in decimal degrees
        :param location_longitude: The longitude to resolve, in decimal degrees
        :param location_shapes: A list of shapefiles to return. Valid options are
                                "NEIGHBORHOOD", "CITY", "STATE", and "COUNTY".
        :return resolved information (holidays, weather, etc)
        """
        if user is not None:
            userResult = copy.copy(user.__dict__)
        else:
            userResult = {}

        to_push = {"apiKey": self.api_key}

        if 'ip' in userResult is not None:
            to_push['ipAddress'] = userResult['ip']
            del userResult['ip']

        if ip is not None:
            to_push['ipAddress'] = ip

        if unixtime is None:
            to_push['unixTimestamp'] = round(time.time())
        else:
            to_push['unixTimestamp'] = unixtime

        additional = userResult

        if 'location' in additional:
            location = additional['location']
        else:
            location = {}

        if location_city is not None:
            location['city'] = location_city

        if location_state is not None:
            location['state'] = location_state

        if location_country is not None:
            location['country'] = location_country

        if location_free_text is not None:
            location['text'] = location_free_text

        if location_latitude is not None:
            location['latitude'] = location_latitude

        if location_longitude is not None:
            location['longitude'] = location_longitude

        if location_shapes is not None:
            location['shapeTypes'] = location_shapes

        additional['location'] = location

        to_push['user'] = {"additional": additional}

        if self.secret is not None:
            self.__signTemporal(to_push)

        response = requests.post(self.service_end_point + "temporaldata", data=json.dumps(to_push))
        if response.status_code != 200:
            raise brein_exception.BreinAPIConnectionError(response)
        result = json.loads(response.text)
        return result

    def getSupportedLookupDimensions(self):
        return validFields.lookup_dimensions

    def __pushActivity__(self, to_push):
        try:
            if self.secret is not None:
                self.__signActivity(to_push)
            res = requests.post(self.service_end_point + "activity",
                                data=json.dumps(to_push))
            return res
        except Exception as e:
            logging.getLogger("breinify").error(e)
            pass

    def __hashSig(self, to_push, message):
        signature = base64.b64encode(
            hmac.new(self.secret.encode("UTF-8"), str(message).encode("UTF-8"), digestmod=hashlib.sha256).digest()) \
            .decode("UTF-8")
        to_push["signature"] = signature
        to_push["signatureType"] = "HmacSHA256"

    def __signActivity(self, to_push):
        message = (to_push["activity"]["type"] + str(to_push["unixTimestamp"]) + "1")
        self.__hashSig(to_push, message)

    def __signLookup(self, to_push):
        if self.secret is None:
            raise brein_exception.noSecretKeyException()
        message = (
            to_push["lookup"]["dimensions"][0] + str(to_push["unixTimestamp"]) + str(len(to_push["lookup"]["dimensions"])))
        self.__hashSig(to_push, message)

    def __signTemporal(self, to_push):
        message = str(to_push["unixTimestamp"]) + "-"
        if "user" in to_push:
            if "additional" in to_push["user"]:
                if "localDateTime" in to_push["user"]["additional"]:
                    message = message + str(to_push["user"]["additional"]["localDateTime"])
        message = message + "-"
        if "user" in to_push:
            if "additional" in to_push["user"]:
                if "timeZone" in to_push["user"]["additional"]:
                    message = message + str(to_push["user"]["additional"]["timeZone"])

        self.__hashSig(to_push, message)

    def __getstate__(self):
        self_dict = self.__dict__.copy()
        del self_dict['pool']
        return self_dict
