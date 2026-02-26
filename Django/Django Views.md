
Django views are Python functions that take http requests and return http response, like HTML documents.

Views are usually put in a file called `views.py` located on your app's folder.

```python
from django.shortcuts import render
from django.http import HttpResponse

def helloworld(request):
    return HttpResponse("Hello world!")
```

This is a simple example on how to send a response back to the browser.