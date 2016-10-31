```python
#create a user you are interested in with their email and last name
example_user = breinify.user(ip="143.127.128.10")

result = breinify.temporal(example_user)

data["weather"]
#{'cloudCover': 12.0, 'windStrength': 1.35, 'description': 'few clouds', 'temperature': 19.427999999999997,
# 'precipitation': {'precipitationType': 'NONE', 'precipitationAmount': 0.0}, 'lastMeasured': 1477523622}

data["location"]
#{'lon': -122.032181, 'city': 'Cupertino', 'country': 'US', 'state': 'CA', 'lat': 37.323002}

data["time"]
# {'epochMinute': 23, 'localYear': 2016, 'epochYear': 2016, 'localHour': 23, 'timezone': 'GMT', 'localDayName':
# 'Saturday', 'epochDayName': 'Saturday', 'epochFormatIso8601': '2016-10-22T23:23:21+00:00', 'epochSecond': 21,
# 'localDay': 22, 'localFormatIso8601': '2016-10-22T23:23:21+00:00', 'localSecond': 21, 'localMinute': 23,
# 'localMonth': 10, 'epochHour': 23, 'epochMonth': 10, 'epochDay': 22, 'epoch': 1477178601}

data["holidays"]
#[] (no holidays today)
```