from breinify import Breinify

apiKey = "938D-3120-64DD-413F-BB55-6573-90CE-473A"

location = "San Francisco, CA"

brein = Breinify(apiKey)

result = brein.temporal_data(location_free_text=location, unixtime=1492344000)

holidays = result['holidays']

if len(holidays) == 0:
    print("There are holidays today.")
else:
    print("Happy %s!"%(holidays[0]['holiday']))