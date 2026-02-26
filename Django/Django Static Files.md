
Websites generally need to serve additional files such as images, JavaScript, or CSS. In Django, we refer to these files as “static files”. Django provides [`django.contrib.staticfiles`](https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/#module-django.contrib.staticfiles "django.contrib.staticfiles: An app for handling static files.") to help you manage them.

### Configuring static files

1. Make sure that `django.contrib.staticfiles` is included in your [`INSTALLED_APPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-INSTALLED_APPS).
    
2. In your settings file, define [`STATIC_URL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-STATIC_URL), for example:
    
    STATIC_URL = "static/"
    
3. In your templates, use the [`static`](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/#std-templatetag-static) template tag to build the URL for the given relative path using the configured `staticfiles` [`STORAGES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-STORAGES) alias.
   ```
   {% load static %}
   <img src="{% static 'my_app/example.jpg' %}" alt="My image">
   ```

4. Store your static files in a folder called `static` in your app. For example `my_app/static/my_app/example.jpg`.


*Note: For some unknown reason {% load static%} shows error in pycharm but works in VScode.*