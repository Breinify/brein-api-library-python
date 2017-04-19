from breinify import Breinify, User

apiKey = "938D-3120-64DD-413F-BB55-6573-90CE-473A"

brein = Breinify(apiKey)

user = User(email="jd@example.com", first_name="John", sessionid="f600757f-3df7-4289-b06c-d2e6de80b6c1", deviceid="aaaabbbbbcccc")
future = brein.send_activity(user, 'login')

print(future.get(timeout=60))
