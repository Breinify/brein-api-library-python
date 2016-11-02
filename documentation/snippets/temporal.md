> ```python
> # Create a user with just their IP address 
> example_user = breinify.user(ip="143.127.128.10")
> 
> result = breinify.temporal_data(example_user)
> 
> weather = result["weather"]
> location = result["location"]
> time = result["time"]
> holidays = result["holidays"]
>
> # Create a user with their IP address, 
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
