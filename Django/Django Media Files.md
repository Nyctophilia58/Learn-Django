
In Django any files that are uploaded by the user are called media files. To load the media files in the browser, we have a special configuration(just like the static files). 

1. Create a folder called media on the root folder. 

2. In `settings.py`:
```
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

3.  Add following snippet to your `urls.py`
```
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

4. Add string representation of the model in `models.py` for an example class `Employee`
```
def __str__(self):

return f'{self.first_name} {self.last_name}'
```

5. Create an employee and check the photo. 