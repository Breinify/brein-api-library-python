import base64
import copy
import hashlib
import hmac
import json
import logging
import requests
import time
from multiprocessing import Pool

from . import BreinExceptions
from . import validFields


class user:
    """
    A specific user on your site
    """

    def __init__(self, **kwargs):
        """
        Potential identifiers for the user. All fields are optional, but additional identifiers may improve the accuracy of the results
        :param email: The user's email
        :param firstname: The user's first name
        :param lastname: The user's last name
        :param dateofbirth: The user's date of birth (MM/DD/YYYY)
        :param imei: A user's cellular device
        :param deviceid: A user's device's unique identifier
        :param sessionid: A web session ID
        :param ip: A user's ip address
        :param agentstring: A user's web browser's user agent string
        """
        validUserFields = ["email", "firstname", "lastName", "dateofbirth", "imei", "deviceid", "sessionid", "ip",
                           "agentstring"]

        for param in validUserFields:
            if kwargs.get(param) is not None:
                self.__dict__[param] = kwargs.get(param)


def setup(api_key, secret=None, service_end_point="https://api.breinify.com/", threadPoolSize=10):
    """Initialize a connection to the Breinify API
    :param api_key: Your API key, available through Breinify.com
    :param secret: Your (optional) secret key to sign calls to the Breinify API
    :param service_end_point: for debugging purposes
    :param threadPoolSize: The number of threads to handle asynchronous activity pushes
    """
    setup.api_key = api_key
    setup.service_end_point = service_end_point
    setup.pool = Pool(processes=threadPoolSize)
    setup.secret = secret


def send_activity(user, activity_type, category, description, tags=None, url=None, referrer=None, activity_time=None):
    """
    Reports a user's activity to the Brein Engine
    :param user: The user who's activity is being reported
    :param activity_type: The type of activity
    :param category: The category of the activity
    :param description: A free text description of the activity
    """
    userResult = copy.copy(user.__dict__)

    toPush = {"apiKey": setup.api_key}

    additional = {}

    if url is not None:
        additional['url'] = url

    if referrer is not None:
        additional['referrer'] = referrer

    if userResult['agentstring'] is not None:
        additional['userAgent'] = userResult['agentstring']
        del userResult['agentstring']

    if userResult['ip'] is not None:
        toPush['ipAddress'] = userResult['ip']
        del userResult['ip']

    if len(additional) > 0:
        userResult['additional'] = additional

    toPush['user'] = userResult

    if activity_time is None:
        toPush['unixTimestamp'] = round(time.time())
    else:
        toPush['unixTimestamp'] = activity_time

    activity = {"type": activity_type, "category": category, "description": description}

    if tags is not None:
        activity['tags'] = tags

    toPush['activity'] = activity

    setup.pool.apply_async(__pushActivity__, (toPush,))


def lookup(user, dimensions):
    """
    Lookup a given user's information
    :param user: The user that you want data about
    :param dimensions: What types of data do you want? (see getSupportedLookupDimensions())
    :param sign: Should we sign this lookup with your secret key?
    :return: A map containing information about each of the specified dimensions for the user
    """
    toPush = {"user": user.__dict__, "lookup": {"dimensions": dimensions}, "apiKey": setup.api_key,
              "unixTimestamp": round(time.time())}
    for dim in dimensions:
        if not dim in getSupportedLookupDimensions():
            raise BreinExceptions.invalidArguementException(dim, getSupportedLookupDimensions())
    if setup.secret is not None:
        __signLookup(toPush)
    response = requests.post(setup.service_end_point + "lookup", data=json.dumps(toPush))
    if response.status_code != 200:
        raise BreinExceptions.BreinAPIConnectionError(response)
    result = json.loads(response.text)
    return result


def getSupportedLookupDimensions():
    return validFields.lookup_dimensions


def __pushActivity__(toPush):
    try:
        res = requests.post(setup.service_end_point + "activity",
                            data=json.dumps(toPush))
        if setup.secret is not None:
            __signActivity(toPush)
        if res.status_code != 200:
            raise BreinExceptions.BreinAPIConnectionError(res)
    except Exception as e:
        logging.getLogger("breinify").error(e)
        pass


def __signActivity(toPush):
    message = (toPush["activity"]["type"] + str(toPush["unixTimestamp"]) + "1").encode("UTF-8")
    signature = base64.b64encode(
        hmac.new(setup.secret.encode("UTF-8"), message, digestmod=hashlib.sha256).digest()).decode("UTF-8")
    toPush["signature"] = signature
    toPush["signatureType"] = "HmacSHA256"


def __signLookup(toPush):
    if setup.secret is None:
        raise BreinExceptions.noSecretKeyException()
    message = (
        toPush["lookup"]["dimensions"][0] + str(toPush["unixTimestamp"]) + str(
            len(toPush["lookup"]["dimensions"]))).encode(
        "UTF-8")
    signature = base64.b64encode(
        hmac.new(setup.secret.encode("UTF-8"), message, digestmod=hashlib.sha256).digest()).decode("UTF-8")
    toPush["signature"] = signature
    toPush["signatureType"] = "HmacSHA256"
