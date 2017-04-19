# Additional Code Samples

## Temporal Knowledge

### About You

Run [`about_you.py`](./about_you.py) to get information about where you are running the script from.

For example, you will get output like:

```
You are in San Francisco, the local time there is 2017-04-18T15:30:55-07:00 and the weather is broken clouds.
```

### IP Address to Local Information

Run [`ip2local.py`](./ip2local.py) to get information a user accessing your site from a given ip address.

For example, you will get output like:

```
204.22.122.60 is in Lansing, MI, the local time there is 2017-04-18T18:32:21-04:00.
```

### Latitude / Longitude to City Name
Run [`point2loc.py`](./point2loc.py) lookup a location based on a latitude/longitude pair.

For example, you will get output like:

```
The point 28.538300,-81.379200 is in Orlando, FL.
```

### Get Major Events for a City

Run [`get_major_events.py`](./get_major_events.py) to get a list of major events happening today in San Francisco.

For example, you will get output like:
```
There are 5 major events happening today in San Francisco, CA
They are:
{'endTime': 1492592400.0, 'displayName': 'Hans Zimmer', 'location': {'zipCode': '94102', 'country': 'US', 'granularity': 'exact', 'lat': '37.7784991', 'city': 'San Francisco', 'state': 'CA', 'lon': '-122.4174670'}, 'startTime': 1492585200.0, 'sizeEstimated': 4.0}
{'displayName': 'Mastodon, Eagles of Death Metal & Russian Circles', 'sizeEstimated': 4.0, 'endTime': 1492572600.0, 'location': {'zipCode': '94102', 'country': 'US', 'granularity': 'exact', 'lat': '37.7824671', 'city': 'San Francisco', 'state': 'CA', 'lon': '-122.4100567'}, 'startTime': 1492565400.0, 'category': 'eventCategoryConcert'}
{'displayName': 'GRAVY TRAIN', 'sizeEstimated': 3.0, 'endTime': 1492579800.0, 'location': {'zipCode': '94110', 'country': 'US', 'granularity': 'exact', 'lat': '37.7553513', 'city': 'San Francisco', 'state': 'CA', 'lon': '-122.4198765'}, 'startTime': 1492572600.0, 'category': 'eventCategoryConcert'}
{'displayName': 'Oceano', 'sizeEstimated': 3.0, 'endTime': 1492576200.0, 'location': {'zipCode': '94103', 'country': 'US', 'granularity': 'exact', 'lat': '37.7709840', 'city': 'San Francisco', 'state': 'CA', 'lon': '-122.4127360'}, 'startTime': 1492569000.0, 'category': 'eventCategoryConcert'}
{'displayName': 'Johann Johannsson', 'sizeEstimated': 3.0, 'endTime': 1492578000.0, 'location': {'zipCode': '94109', 'country': 'US', 'granularity': 'exact', 'lat': '37.7879318', 'city': 'San Francisco', 'state': 'CA', 'lon': '-122.4216895'}, 'startTime': 1492570800.0, 'category': 'eventCategoryConcert'}
```

### Find Holidays

Run [`get_holiday.py`](./get_holiday.py) to get a holiday greeting.

For example, you will get output like:
```
Happy Easter Sunday!
```


### Visualize Locations

Run [`point2shape.py`](./point2shape.py) to get the shapes of the state that a give point is in. Note that matplotlib is required
which you can get by running `pip3 install matplotlib`.

Your output should look like:
![The expected output](https://raw.githubusercontent.com/Breinify/brein-api-library-python/master/documentation/img/florida.png "")



## Activities

### User Makes Purchase

See [`send_purchase_activity.py`](./send_purchase_activity.py) for an example of how to log that a user purchased something. The `send_activity`
function runs asynchronously and returns an `ApplyResult` object.

Your output will be:

```
<Response [200]>
```

If you are signed up for our analytics service and used your api key, then you will be able to see the activity on your dashboard also.

### User Registers

See [`send_register_activity.py`](./send_register_activity.py) for an example of how to log that a user has registered or logged in. The `send_activity`
function runs asynchronously and returns an `ApplyResult` object.

Your output will be:

```
<Response [200]>
```

If you are signed up for our analytics service and used your api key, then you will be able to see the activity on your dashboard also.
