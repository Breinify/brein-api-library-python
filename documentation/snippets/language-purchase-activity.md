>
```python
s_id = 'f600757f-3df7-4289-b06c-d2e6de80b6c1'
tags = {
    'productIds': ['125689', '982361', '157029'],
    'productPrices': [134.23, 15.13, 12.99]
}
user = User(sessionid=s_id)
brein.send_activity(user, 'checkOut', tags=tags)
```