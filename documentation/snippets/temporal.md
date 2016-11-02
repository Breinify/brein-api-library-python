>
```python
#create a user you are interested in with their email and last name
example_user = breinify.user(ip="143.127.128.10")

result = breinify.temporal_data(example_user)

result["weather"]
#{'cloudCover': 12.0, 'windStrength': 1.35, 'description': 'few clouds', 'temperature': 19.427999999999997,
# 'precipitation': {'precipitationType': 'NONE', 'precipitationAmount': 0.0}, 'lastMeasured': 1477523622}

result["location"]
#'location': {'country': 'US', 'state': 'CA', 'lat': 37.366051, 'city': 'San Jose', 'granularity': 'city',
#  'lon': -121.827179}

result["time"]
# 'time': {'localHour': 12, 'localMinute': 54, 'timezone': 'America/Los_Angeles', 'localYear': 2016, 'epochYear': 2016,
# 'localDayName': 'Monday', 'epoch': 1477943668, 'epochMonth': 10, 'localFormatIso8601': '2016-10-31T12:54:28-07:00',
# 'localSecond': 28, 'localDay': 31, 'epochDay': 31, 'epochDayName': 'Monday', 'epochSecond': 28, 'localMonth': 10,
# 'epochFormatIso8601': '2016-10-31T19:54:28+00:00', 'epochMinute': 54, 'epochHour': 19}

result["holidays"]
#'holidays': [{'holiday': 'World Cities Day', 'source': 'United Nations', 'types': ['SPECIAL_DAY']},
# {'holiday': 'Halloween', 'source': 'Public Information', 'types': ['HALLMARK']}]}
```
