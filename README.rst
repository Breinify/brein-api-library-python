.. raw:: html

   <p align="center"><img src="https://www.breinify.com/img/Breinify_logo.png" alt="Breinify API Python Library" width="250"></p>

.. raw:: html

   <div> <a href="https://pypi.python.org/pypi/brein-api/"><img src="https://img.shields.io/pypi/v/brein-api.svg" alt = "Current Version" style="float: left;"/></a> &nbsp; <a href="https://github.com/Breinify/brein-api-library-python/blob/master/LICENSE"><img src="https://img.shields.io/pypi/l/brein-api.svg" alt = "MIT"/></a></div>


This library simplifies access to Breinify's API for tasks like geocoding, reverse geocoding, weather and events look up, and holidays determination based on information such as a user's ip address, coordinates, or reported location.  In addition, this documentation gives detailed examples for each of the features available for the different endpoints.

*TemporalData Endpoint:* The endpoint offers features to resolve temporal information like a timestamp, a location (latitude and longitude or free-text), or an IP-address, to temporal information (e.g., timezone, epoch, formatted dates, day-name), holidays at the specified time and location, city, zip-code, neighborhood, country, or county of the location, events at the specified time and location (e.g., description, size, type), weather at the specified time and location (e.g., description, temperature).

*Activity Endpoint:* The endpoint is used to understand the usage-patterns and the behavior of a user using, e.g., an application, a mobile app, or a web-browser. The endpoint offers analytics and insights through Breinify's dashboard.

Quick start
===========

Step 1: Download the Library
----------------------------
Download the library from PyPi and install it with

.. code:: bash

    pip3 install brein-api

or download the source from github and run

.. code:: python

    python3 setup.py install


Step 2: Integrate the library
-----------------------------
Integrate the Library into your Python 3 project by importing the library in the relevant blocks of code.

.. code:: python

    import breinify



Step 3: Configure the library
-----------------------------

In order to use the library you need a valid API-key, which you can get for free at https://www.breinify.com. In this example, we assume you have the following api-key:

**938D-3120-64DD-413F-BB55-6573-90CE-473A**

.. code:: python

    from breinify import Breinify

    ##this is a valid API key
    apiKey = "938D-3120-64DD-413F-BB55-6573-90CE-473A"

    brein = Breinify(apiKey)


The Breinify class is now configured with a valid configuration object.


Step 4: Start using the library
-------------------------------

Temporal Data Lookup
^^^^^^^^^^^^^^^^^^^^


Looking Up a User's Location's Info
+++++++++++++++++++++++++++++++++++

You may want to customize the user's experience based on where they are. For example calling

.. code:: python

    #create a user you are interested in based on their ip. Other fields (coordinates, time, etc) can also be included
    example_user = User(ip="143.127.128.10")

    result = brein.temporal_data(example_user)

will result in a dictionary of timely information for the location the ip address resolves to (San Jose), for example:

.. code:: python

    #wrap the result in json.dumps() for readability
    print(json.dumps(result,indent=4))

Which will print something similar to:

.. raw:: html

   <p align="center"><img src="https://raw.githubusercontent.com/Breinify/brein-api-library-python/master/documentation/img/sample_response.png" alt="sample output" width="400"></p>


Looking Up Information About a Location
+++++++++++++++++++++++++++++++++++++++

Instead of looking up information based off a user's location, you can just supply the location's information directly.
For example, you could get yesterday's weather in San Francisco by running:

.. code:: python

    from breinify import Breinify
    import time
    import math

    apiKey = "938D-3120-64DD-413F-BB55-6573-90CE-473A"

    brein = Breinify(apiKey)

    yesterday = math.floor(time.time()) - 24*60*60

    result = brein.temporal_data(location_free_text="San Francisco, CA", unixtime = yesterday)

    print("Yesterday in %s, the weather was %s with a temperature of %d F."%(result['location']['city'], result['weather']['description'], result['weather']['temperatureF']))

Which will print something similar to "Yesterday in San Francisco, the weather was overcast clouds with a temperature of 64 F."


Placing activity triggers
^^^^^^^^^^^^^^^^^^^^^^^^^

The engine powering the DigitalDNA API provides three endpoints. The first endpoint is used to inform the engine about the activities performed by visitors of your site. The activities are used to understand the user's current interest and infer the intent. It becomes more and more accurate across different users and verticals as more activities are collected. It should be noted, that any personal information is not stored within the engine, thus each individual's privacy is well protected. The engine understands several different activities performed by a user, e.g., landing, login, search, item selection, or logout.

For this example, pretend that a user named "John Doe" is logged in to your site with his email address (john.doe@email.com) is viewing the page "www.example.com". You can log this by executing:

.. code:: python

    from breinify import User
    #create a user you are interested in with their email and last name
    example_user = User(email="john.doe@email.com")

    brein.send_activity(example_user, "pageView", url="www.example.com")

The call will then be run asynchronously in the background.


Further links
-------------

To understand all the capabilities of Breinify's DigitalDNA API, take a look at:

*  `Additional Code Examples`__.

.. __: https://github.com/Breinify/brein-api-library-python/tree/master/documentation/additional

*  `Breinify's Website`__.

.. __: https://www.breinify.com
