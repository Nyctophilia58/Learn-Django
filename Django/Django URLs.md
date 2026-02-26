
Create a file named `urls.py` in the same folder as the `views.py` file, and type this code in it:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.helloworld, name='helloworld'),
]
```

The `urls.py` file you just created is specific for the `helloworld` application. We have to do some routing in the root directory `my_app` as well. 

There is a file called `urls.py` on the `my_app` folder, open that file and add the `include` module in the `import` statement, and also add a `path()` function in the `urlpatterns[]` list, with arguments that will route users that comes in via `127.0.0.1:8000/`.