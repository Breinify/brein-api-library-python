from breinify import Breinify
apiKey = "938D-3120-64DD-413F-BB55-6573-90CE-473A"

brein = Breinify(apiKey)

result = brein.temporal_data()

print("You are in %s, the local time there is %s and the weather is %s." % (result['location']['city'],result['time']['localFormatIso8601'], result['weather']['description']))
