import base64
import hashlib
import hmac
import json
import requests
import time
from multiprocessing import Pool


class user:
    def __init__(self, email, firstname=None, lastname=None, dateofbirth=None, imei=None, deviceid=None,
                 sessionid=None):
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


##TODO: return something other than True if something bad happens!
def connect(api_key, service_end_point="https://api.breinify.com/", threadPoolSize=10):
    ###Initialize a connection to the Breinify API
    connect.api_key = api_key
    connect.service_end_point = service_end_point
    connect.pool = Pool(processes=threadPoolSize)
    return True


def setSecret(secret):
    connect.secret = secret

def getSupportedLookupFields():
    return ["email", "first name", "last name"]


def getSupportedActivityTypes():
    return ["search", "login", "logout", "addToCart", "removeFromCart", "selectProduct", "checkOut", "other"]


def getSupportedCategories():
    return ["home", "education", "family", "food", "health", "job", "services", "other"]


def __pushActivity__(toPush, sign):
    res = requests.post(connect.service_end_point + "activity",
                        data=json.dumps(toPush))
    if sign:
        __signActivity(toPush)
    return res


def __signActivity(toPush):
    message = (toPush["activity"]["type"] + str(toPush["unixTimestamp"]) + "1").encode("UTF-8")
    signature = base64.b64encode(
        hmac.new(connect.secret.encode("UTF-8"), message, digestmod=hashlib.sha256).digest()).decode("UTF-8")
    toPush["signature"] = signature
    toPush["signatureType"] = "HmacSHA256"


def activity(user, activity_type, category, description, sign=False):
    ##TODO: category+descriptions!
    toPush = {"user": user.__dict__, "activity": {"type": activity_type}, "apiKey": connect.api_key,
              "unixTimestamp": round(time.time())}
    connect.pool.apply_async(__pushActivity__, (toPush, sign,))
    return


def __signLookup(toPush):
    message = (
    toPush["lookup"]["dimensions"][0] + str(toPush["unixTimestamp"]) + str(len(toPush["lookup"]["dimensions"]))).encode(
        "UTF-8")
    signature = base64.b64encode(
        hmac.new(connect.secret.encode("UTF-8"), message, digestmod=hashlib.sha256).digest()).decode("UTF-8")
    toPush["signature"] = signature
    toPush["signatureType"] = "HmacSHA256"


def lookup(user, fields, sign=False):
    toPush = {"user": user.__dict__, "lookup": {"dimensions": fields}, "apiKey": connect.api_key,
              "unixTimestamp": round(time.time())}
    if sign:
        __signLookup(toPush)
    response = requests.post(connect.service_end_point + "lookup", data=json.dumps(toPush))
    if response.status_code != 200:
        raise ConnectionError("Non-normal lookup response: " + str(response.status_code), response)
    result = json.loads(response.text)
    return result
