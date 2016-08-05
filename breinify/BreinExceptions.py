class BreinAPIConnectionError(ConnectionError):
    def __init__(self, response):
        super(BreinAPIConnectionError, self).__init__("Non-normal lookup response: " + str(response.status_code),
                                                      response)


class invalidArguementException(ValueError):
    def __init__(self, value, expected):
        super(invalidArguementException, self).__init__("Got '" + str(value) + "' expected one of " + str(expected),
                                                        value)


class noSecretKeyException(ValueError):
    def __init__(self):
        super(noSecretKeyException, self).__init__(
            "Tried to sign message, but no secret key found. Either disable signing or call breinify.setSecret(...)")
