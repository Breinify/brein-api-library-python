import breinify
import json


def printAt(location):
    """
    Prints out a json of useful information about the given location.
    :param location: A string describing a US city.
    :return: The city's dictionary
    """
    brein = breinify.Breinify("YOURAPIKEY")
    result = brein.temporal_data(location_free_text = location)
    print("Information for "+location+":")
    print("-----------------------------")
    print(json.dumps(result,indent=4))
    return result


if __name__ == '__main__':
    printAt("san francisco, ca")
    printAt("nyc")
