from breinify import Breinify, User

apiKey = "938D-3120-64DD-413F-BB55-6573-90CE-473A"

brein = Breinify(apiKey)

tags = {
    #List of products purchased
    'productIds': [ '125689', '982361', '157029' ],
    #List of prices for those products
    'productPrices': [ 134.23, 15.13, 12.99 ]
}
user = User(email = "jd@example.com", first_name = "John")
future = brein.send_activity(user, 'checkOut', tags = tags)

print(future.get(timeout=60))