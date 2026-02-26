
The moment you create an app you need to add it in the `INSTALLED_APPS`
#### To create a database: 

```python
python manage.py makemigrations
python manage.py migrate
```

***`makemigrations`***: 
	Reads your `models.py`, look for any changes or any modifications or any newly created classes and create a migration file. This command only generates the SQL commands.

***`migrate`***:
	This command actually executes the SQL commands. 

Inside the apps `admin.py` we need to register the model that we've created. 

#### To Register: 

```python
from django.contrib import admin

from .models import ModelName

# Register your models here.

admin.site.register(Modelname)
```


***Note**: You can view the SQL statement that were executed from the migration above. All you have to do is to run this command, with the migration number: `python manage.py sqlmigrate members 0001`*
