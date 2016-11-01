>
```python
    import breinify
    apiKey = "time-is-ticking" 
    breinify.setup(apiKey)
```

```
If you configured your key with our dashboard to require a signature, please add the following
```

>
```python
    secret = "time-rift"
    breinify.setup(apiKey, secret)
```