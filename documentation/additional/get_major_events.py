from breinify import Breinify

apiKey = "938D-3120-64DD-413F-BB55-6573-90CE-473A"

location = "San Francisco, CA"

brein = Breinify(apiKey)

result = brein.temporal_data(location_free_text=location)

events = list(filter(lambda event: event['sizeEstimated'] >= 3, result['events']))

if len(events) == 0:
    print("There are no major events happening today in %s"%(location))
else:
    print("There are %s major events happening today in %s"%(len(events), location))
    print("They are:")
    for event in events:
        print(event)