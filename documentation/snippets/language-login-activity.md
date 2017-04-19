>
```python
s_id = 'f600757f-3df7-4289-b06c-d2e6de80b6c1'
email = 'max@sample.com' #typically read from an input field
user = User(email=email, sessionid=s_id)
brein.send_activity(user, 'login')
```