from breinify import Breinify

apiKey = "938D-3120-64DD-413F-BB55-6573-90CE-473A"

lat = 28.5383
lon = -81.3792

brein = Breinify(apiKey)

result = brein.temporal_data(location_longitude=lon, location_latitude=lat)

##should be Orlando
print("The point %f,%f is in %s, %s." % (lat, lon, result['location']['city'], result['location']['state']))
