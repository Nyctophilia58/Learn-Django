
The next step is to configure the root URLconf in the `mysite` project to include the URLconf defined in apps urls(for example, `polls.urls`). To do this, add an import for `django.urls.include` in `mysite/urls.py` and insert an [`include()`](https://docs.djangoproject.com/en/6.0/ref/urls/#django.urls.include "django.urls.include") in the `urlpatterns` list, so you have:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

The [`path()`](https://docs.djangoproject.com/en/6.0/ref/urls/#django.urls.path "django.urls.path") function expects at least two arguments: `route` and `view`. The [`include()`](https://docs.djangoproject.com/en/6.0/ref/urls/#django.urls.include "django.urls.include") function allows referencing other URLconfs. Whenever Django encounters [`include()`](https://docs.djangoproject.com/en/6.0/ref/urls/#django.urls.include "django.urls.include"), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.