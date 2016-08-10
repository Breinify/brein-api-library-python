```python
result = breinify.lookup(example_user,["firstname","gender"])
## should return "{'gender': {'result': 'MALE', 'accuracy': 1.0},
##              'firstname': {'result': 'John', 'accuracy': 0.92}}"
name = result["firstname"]["result"]
honorific = " "
if result["gender"]["result"]=='MALE' and result["gender"]["accuracy"] > 0.80:
    honorific = " Mr. "
if result["gender"]["result"]=='FEMALE' and result["gender"]["accuracy"] > 0.80:
    honorific = " Mrs. "
if result["firstname"]["accuracy"] < 0.8: #don't customize if we're not sure about their name
    honorific = ""
    name = ""
print("Hi"+honorific+name+"! What can we at Breinify do for you today?")
##should print "Hi Mr. John! What can we at Breinify do for you today?"
```