>
```python
sId = '111222233334444'
tags = {
    'productIds': [ '125689', '982361', '157029' ],
    'productPrices': [ 134.23, 15.13, 12.99 ]
}

user = User(sessionid = s_id)

brein.send_activity(user, 'checkOut', tags = tags)
```