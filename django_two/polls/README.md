# Path function in urls.py
What's this?
`path('', views.index, name='index')`

## 1. ''
Like /route/ from
`https://www.example.com/polls/route/?page=3`
considering this urls.py was included like `include('polls.urls')`

## 2. views.index
This is the function that receives a `HttpRequest` and returns a `HttpResponse`. Much intuitive.

Refer to `views.py`

We can assume that `HttpResponse` is like the webpage. How to send a fancy.html page? Coming soon I guess...

## 3. 
You know... this is taking a bit too much time...

## Reference
[Part 1](https://docs.djangoproject.com/en/2.0/intro/tutorial01/)
