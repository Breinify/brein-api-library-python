```python
result = breinify.lookup(example_user,["firstname", "gender", "age", "agegroup", "digitalfootprint", "images"])

name = result["firstname"]["result"]
name_accuracy = result["firstname"]["accuracy"]

gender = result["gender"]["result"]
gender_accuracy = result["gender"]["accuracy"]

age = result["age"]["result"]
age_accuracy = result["age"]["accuracy"]

agegroup = result["agegroup"]["result"]
agegroup_accuracy = result["agegroup"]["accuracy"]

digitalfootprint = result["digitalfootprint"]["result"]
digitalfootprint_accuracy = result["digitalfootprint"]["accuracy"]

images = result["images"]["result"]
images_accuracy = result["images"]["accuracy"]
```