To authorize, use this code:

> ```shell
> #install via pip
> pip3 install brein-api
> ```

> ```python
> import breinify
>
> apiKey = "time-is-ticking"
> breinify.setup(apiKey)
> ```

If you configured your api key to require a signature, please use the following:

> ```python
> import breinify
>
> apiKey = "time-is-ticking"
> secretKey = "time-rift"
> breinify.setup(apiKey, secretKey)
> ```
