>
```python
#create a user you are interested in with their email and last name
example_user = breinify.user(email="ziggy@email.com",
                             firstname="David",
                             dateofbirth="1/18/1974",
                             imei="999867530900000",
                             deviceid="9b20a397-d0b6-4264-acf9-4b937e2a98df",
                             sessionid="3d16a9b2e0456a29d27a2c5fef040910",
                             ip="107.182.162.21",
                             agentstring="Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21."+
                             "10 (KHTML, like Gecko) Mobile/7B405")

breinify.send_activity(example_user,
                       "viewpage",
                       "apparel",
                       "White Summer shirt (M)",
                       tags={"size":"medium", "color":"white"},
                       url="https://shop.breinify.com/browse/shirts/549.html",
                       referrer="google.com")
```
