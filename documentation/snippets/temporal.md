> ```python
> # Example with just IP address set 
> example_user = breinify.user(ip="143.127.128.10")
> 
> result = breinify.temporal_data(example_user)
> 
> weather = result["weather"]
> location = result["location"]
> time = result["time"]
> holidays = result["holidays"]
> ```
