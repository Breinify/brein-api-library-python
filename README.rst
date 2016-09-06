.. image:: https://raw.githubusercontent.com/Breinify/brein-api-library-python/master/documentation/img/logo250px.png
    :align: center
    :alt: Breinify API Python Library

.. class:: center

Breinify's DigitalDNA API puts dynamic behavior-based, people-driven data right at your fingertips.


Step By Step Introductions
==========================

What is Breinify's DigitialDNA
------------------------------

Breinify's DigitalDNA API puts dynamic behavior-based, people-driven data right at your fingertips. We believe that in many situations, a critical component of a great user experience is personalization. With all the data available on the web it should be easy to provide a unique experience to every visitor, and yet, sometimes you may find yourself wondering why it is so difficult.

Thanks to **Breinify's DigitalDNA** you are now able to adapt your online presence to your visitors needs and **provide a unique experience**. Let's walk step-by-step through a simple example.

Quick start
===========

Step 1: Download the Library
----------------------------
Download the library from PyPi and install it with

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

**772A-47D7-93A3-4EA9-9D73-85B9-479B-16C6**

.. code:: python

    ##this is a valid API key
    apiKey = "772A-47D7-93A3-4EA9-9D73-85B9-479B-16C6"

    breinify.setup(apiKey)

The Breinify class is now configured with a valid configuration object.


Step 4: Start using the library
-------------------------------

Placing activity triggers
^^^^^^^^^^^^^^^^^^^^^^^^^

The engine powering the DigitalDNA API provides two endpoints. The first endpoint is used to inform the engine about the activities performed by visitors of your site. The activities are used to understand the user's current interest and infer the intent. It becomes more and more accurate across different users and verticals as more activities are collected. It should be noted, that any personal information is not stored within the engine, thus each individual's privacy is well protected. The engine understands several different activities performed by a user, e.g., landing, login, search, item selection, or logout.

For this example, pretend that a user named "John Doe" is logged in to your site with his email address (john.doe@email.com) and is searching for a B2B big data company. You can log this activity with the Breinify API using the following code:

.. code:: python

    #create a user you are interested in with their email and last name
    example_user = breinify.user(email="john.doe@email.com");

    breinify.send_activity(user,"search","services","b2b big data companies")

That's it! The call will be run asynchronously in the background. All fields in the user class are optional, but the more data you can supply, the more accurate the results will be.


Placing look-up triggers
^^^^^^^^^^^^^^^^^^^^^^^^

Some time later, you may want to send a message to this user, but you only have their email address. You can query the Breinify lookup API to find necessary fields to personalize the message.

.. code:: python

    result = breinify.lookup(example_user,["firstname","gender"])
    ## should return "{'gender': {'result': 'MALE', 'accuracy': 1.0},
    ##              'firstname': {'result': 'John', 'accuracy': 0.92}}"
    name = result["firstname"]["result"]
    honorific = " "
    if result["gender"]["result"]=='MALE' and result["gender"]["accuracy"] > 0.80:
        honorific = " Mr. "
    if result["gender"]["result"]=='FEMALE' and result["gender"]["accuracy"] > 0.80:
        honorific = " Mrs. "
    if result["firstname"]["accuracy"] < 0.8: #don't customize if we're not sure about their name
        honorific = ""
        name = ""
    print("Hi"+honorific+name+"! What can we at Breinify do for you today?")
    ##should print "Hi Mr. John! What can we at Breinify do for you today?"

A demonstration function is available in demo.py.

With Breinify's advanced artificial intelligence engine, you were able to customize a user's experience and probably increase their engagement with just a few lines of code!

Further links
-------------

To understand all the capabilities of Breinify's DigitalDNA API, take a look at:


*  `Breinify's Website`__.

.. __: https://www.breinify.com
