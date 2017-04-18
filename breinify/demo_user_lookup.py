from breinify import Breinify, User

def fancy_print(email):
    """
    Generates a sample email based of an email address
    :param email: The user's email address
    """
    brein = Breinify("YOURAPIKEY")
    result = brein.lookup(User(email=email), ["firstname", "gender"])
    name = result["firstname"]["result"]
    honorific = " "
    if result["gender"]["result"] == 'MALE' and result["gender"]["accuracy"] > 0.80:
        honorific = " Mr. "
    if result["gender"]["result"] == 'FEMALE' and result["gender"]["accuracy"] > 0.80:
        honorific = " Mrs. "
    if result["firstname"]["accuracy"] < 0.80:
        ##if we aren't sure about their gender, don't guess it!
        honorific = ""
        name = ""
    print("Hi" + honorific + name + "! What can we at Breinify do for you today?")


if __name__ == '__main__':
    fancy_print("john.doe@email.com")
