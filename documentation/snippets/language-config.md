<blockquote class="lang-specific python">
<p>To configure the Python library, either supply your API key:</p>
</blockquote>

>
```python
from breinify import Breinify
brein = Breinify('938D-3120-64DD-413F-BB55-6573-90CE-473A')
```

<blockquote class="lang-specific python">
<p>or with an API key and the key's secret, if required</p>
</blockquote>

>
```python
brein = Breinify('938D-3120-64DD-413F-BB55-6573-90CE-473A',
                 'utakxp7sm6weo5gvk7cytw==')
```

<blockquote class="lang-specific python">
<p>It is recommended that you configure a secret key for use with the Python library.</p>
</blockquote>