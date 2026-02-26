
## Create Templates

Create a `templates` folder inside the `my_app` folder, create a HTML file named `myfirst.html`. 

## Modify The View

```python
from django.http import HttpResponse
from django.template import loader

def helloworld(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())
```

## Change Settings

Look up the `INSTALLED_APPS[]` list and add the `my_app` app like this:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_app'
]
```

Then find `TEMPLATES` -> `'DIRS': []`  and write `'templates'` (the name of your folder) in it.

Then run these commands:

```python
python manage.py migrate
python manage.py runserver
```
