from breinify import Breinify

apiKey = "938D-3120-64DD-413F-BB55-6573-90CE-473A"

ipaddress = "204.22.122.60"

brein = Breinify(apiKey)

result = brein.temporal_data(ip=ipaddress)

print("%s is in %s, %s, the local time there is %s." % (
ipaddress, result['location']['city'], result['location']['state'], result['time']['localFormatIso8601']))
