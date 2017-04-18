<blockquote class="lang-specific python">
<p>The Python library supports calls to temporal data by either passing a user object for a user who's location you want
to get information about</p></blockquote>

>
```python
user = breinify.user(ip = "75.123.012.123")

info = brein.temporal_data(user = user)
```

<blockquote class="lang-specific python">
<p> or a description of the location itself.</p>
</blockquote>

>
```python
info = brein.temporal_data(location_free_text = "san francisco, ca", unixtime = 1492538271)
```

