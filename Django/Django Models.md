
Django by default comes with the SQLite3 database. In `settings.py` there is already sqlite3 database configuration. 

Now we need tables and fields. To create tables we go to `models.py`. 

### Example

```python
from django.db import models

class Employee(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	photo = models.ImageField(upload_to='images')
	designation = models.CharField(max_length=100)
	email_address = models.EmailField(max_length=100, unique=True)
	phone_number = models.CharField(max_length=12, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_add=True)
```

*Note: `auto_now_add` is for one time modification of a field and `auto_now` is good for whenever you need a field to change the instance will be changed.*
