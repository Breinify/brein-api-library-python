import base64
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

    def __init__(self, email=None, firstname=None, lastname=None, dateofbirth=None, imei=None, deviceid=None,
                 sessionid=None):
        """
        Potential identifiers for the user. All fields are optional, but additional identifiers may improve the accuracy of the results
        :param email: The user's email
        :param firstname: The user's first name
        :param lastname: The user's last name
        :param dateofbirth: The user's date of birth (MM/DD/YYYY)
        :param imei: A user's cellular device
        :param deviceid: A user's device's unique identifier
        :param sessionid: A web session ID
        """
        if email != None:
            self.email = email
        ##don't store None values (it'll make the jsons smaller!)
        if firstname != None:
            self.firstName = firstname
        if lastname != None:
            self.lastName = lastname
        if dateofbirth != None:
            self.dateOfBirth = dateofbirth
        if imei != None:
            self.imei = imei
        if deviceid != None:
            self.deviceId = deviceid
        if sessionid != None:
            self.sessionId = sessionid


def connect(api_key, service_end_point="https://api.breinify.com/", threadPoolSize=10):
    """Initialize a connection to the Breinify API
    :param api_key: Your API key, available through Breinify.com
    :param service_end_point: for debugging purposes
    :param threadPoolSize: The number of threads to handle asynchronous activity pushes
    """
    connect.api_key = api_key
    connect.service_end_point = service_end_point
    connect.pool = Pool(processes=threadPoolSize)


def activity(user, activity_type, category, description, sign=False):
    """
    Reports a user's activity to the Brein Engine
    :param user: The user who's activity is being reported
    :param activity_type: The type of activity (See getSupportedActivityTypes())
    :param category: The category of the activity (See getSupportedCategoryTypes())
    :param description: A free text description of the activity
    :param sign: Should we sign the activity with your secret key?
    """
    if connect.secret is None and sign:
        raise BreinExceptions.noSecretKeyException()
    if not activity_type in getSupportedActivityTypes():
        raise BreinExceptions.invalidArguementException(activity_type, getSupportedActivityTypes())
    if not category in getSupportedCategories():
        raise BreinExceptions.invalidArguementException(category, getSupportedCategories())
    toPush = {"user": user.__dict__,
              "activity": {"type": activity_type, "category": category, "description": description},
              "apiKey": connect.api_key,
              "unixTimestamp": round(time.time())}
    connect.pool.apply_async(__pushActivity__, (toPush, sign,))


def lookup(user, dimensions, sign=False):
    """
    Lookup a given user's information
    :param user: The user that you want data about
    :param dimensions: What types of data do you want? (see getSupportedLookupDimensions())
    :param sign: Should we sign this lookup with your secret key?
    :return: A map containing information about each of the specified dimensions for the user
    """
    toPush = {"user": user.__dict__, "lookup": {"dimensions": dimensions}, "apiKey": connect.api_key,
              "unixTimestamp": round(time.time())}
    for dim in dimensions:
        if not dim in getSupportedLookupDimensions():
            raise BreinExceptions.invalidArguementException(dim, getSupportedLookupDimensions())
    if sign:
        __signLookup(toPush)
    response = requests.post(connect.service_end_point + "lookup", data=json.dumps(toPush))
    if response.status_code != 200:
        raise BreinExceptions.BreinAPIConnectionError(response)
    result = json.loads(response.text)
    return result


##only reset secret once
connect.secret = None

def setSecret(secret):
    connect.secret = secret


def getSupportedLookupDimensions():
    return validFields.lookup_dimensions

def getSupportedActivityTypes():
    return validFields.activities

def getSupportedCategories():
    return validFields.categories

def __pushActivity__(toPush, sign):
    try:
        res = requests.post(connect.service_end_point + "activity",
                            data=json.dumps(toPush))
        if sign:
            __signActivity(toPush)
        if res.status_code != 200:
            raise BreinExceptions.BreinAPIConnectionError(res)
    except Exception as e:
        logging.getLogger("breinify").error(e)
        pass


def __signActivity(toPush):
    message = (toPush["activity"]["type"] + str(toPush["unixTimestamp"]) + "1").encode("UTF-8")
    signature = base64.b64encode(
        hmac.new(connect.secret.encode("UTF-8"), message, digestmod=hashlib.sha256).digest()).decode("UTF-8")
    toPush["signature"] = signature
    toPush["signatureType"] = "HmacSHA256"


def __signLookup(toPush):
    if connect.secret is None:
        raise BreinExceptions.noSecretKeyException()
    message = (
    toPush["lookup"]["dimensions"][0] + str(toPush["unixTimestamp"]) + str(len(toPush["lookup"]["dimensions"]))).encode(
        "UTF-8")
    signature = base64.b64encode(
        hmac.new(connect.secret.encode("UTF-8"), message, digestmod=hashlib.sha256).digest()).decode("UTF-8")
    toPush["signature"] = signature
    toPush["signatureType"] = "HmacSHA256"