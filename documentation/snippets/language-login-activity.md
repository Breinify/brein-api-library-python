>
```python
from breinify import user

s_id = '111222233334444'
email = 'max@sample.com' #typically read from an input field

u = user(email = email, sessionid = s_id)

brein.send_activity(user, 'login')
```