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
>
> # Example with IP address, timezone and localdata time 
> example_user = breinify.user(ip="143.127.128.10",
>                              timeZone="America/New_York",
>                              localDateTime="Wed Oct 26 2016 13:02:06 GMT-0700 (EDT)",
>                              location={"longitude"=-73.935242, "latitude"=40.730610})
> 
> result = breinify.temporal_data(example_user)
> 
> weather = result["weather"]
> location = result["location"]
> time = result["time"]
> holidays = result["holidays"]
> ```
