<p align="center">
  <img src="https://raw.githubusercontent.com/Breinify/brein-api-library-python/master/documentation/img/logo.png" alt="Breinify API Python Library" width="250">
</p>

<p align="center">
Breinify's DigitalDNA API puts dynamic behavior-based, people-driven data right at your fingertips.
</p>

### Step By Step Introduction

#### What is Breinify's DigitialDNA

Breinify's DigitalDNA API puts dynamic behavior-based, people-driven data right at your fingertips. We believe that in many situations, a critical component of a great user experience is personalization. With all the data available on the web it should be easy to provide a unique experience to every visitor, and yet, sometimes you may find yourself wondering why it is so difficult.

Thanks to **Breinify's DigitalDNA** you are now able to adapt your online presence to your visitors needs and **provide a unique experience**. Let's walk step-by-step through a simple example.

### Quick start

#### Step 1: Download the Library

Download the wheel from <<more details to come>> and install it with ...


#### Step 2: Integrate the library

Integrate the Library into your Python 3 project. 


#### Step 3: Configure the library

In order to use the library you need a valid API-key, which you can get for free at [https://www.breinify.com](https://www.breinify.com). In this example, we assume you have the following api-key:

**772A-47D7-93A3-4EA9-9D73-85B9-479B-16C6**

```python
##this is a valid API key
apiKey = "772A-47D7-93A3-4EA9-9D73-85B9-479B-16C6"

breinify.connect(apiKey)
## Will always return True

```

The Breinify class is now configured with a valid configuration object.


#### Step 4: Start using the library

##### Placing activity triggers

The engine powering the DigitalDNA API provides two endpoints. The first endpoint is used to inform the engine about the activities performed by visitors of your site. The activities are used to understand the user's current interest and infer the intent. It becomes more and more accurate across different users and verticals as more activities are collected. It should be noted, that any personal information is not stored within the engine, thus each individual's privacy is well protected. The engine understands several different activities performed by a user, e.g., landing, login, search, item selection, or logout.

The engine is informed of an activity by executing *breinify.activity(...)*.

```python
# create a user you are interested in with their email (mandatory field) and any additional identification you want to pass
user = breinify.user("user.anywhere@email.com",lastname = "anywhere");

breinify.activity(user,"search","home","your activity description")

```

That's it! The call will be run asynchronously in the background.


##### Placing look-up triggers

Look-ups are used to retrieve dedicated information for a given user. 

```python
# define an array of subjects of interest
dimensions = ["firstname",
       "gender",
       "age",
       "agegroup",
       "digitalfootprint",
       "images"]

result = breinify.lookup(user, dimensions);

```

### Further links
To understand all the capabilities of Breinify's DigitalDNA API, take a look at:

* [Additional code snippets](documentation/more-snippets.md), or
* [Breinify's Website](https://www.breinify.com).
