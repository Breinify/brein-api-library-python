import breinify

breinify.setup("YOURAPIKEY")


def fancy_print(email):
    result = breinify.lookup(breinify.user(email=email), ["firstname", "gender"])
    name = result["firstname"]["result"]
    honorific = " "
    if result["gender"]["result"] == 'MALE' and result["gender"]["accuracy"] > 0.80:
        honorific = " Mr. "
    if result["gender"]["result"] == 'FEMALE' and result["gender"]["accuracy"] > 0.80:
        honorific = " Mrs. "
    if result["firstname"]["accuracy"] < 0.80:
        ##if we aren't sure about their name, don't guess it!
        honorific = ""
        name = ""
    print("Hi" + honorific + name + "! What can we at Breinify do for you today?")


fancy_print("john.doe@email.com")
