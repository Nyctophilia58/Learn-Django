
An app is a web application that has a specific meaning in your project, like a home page, a contact form, or a members database.

We use apps for building a specific feature. 
### To create app: 

```python
python manage.py startapp appname
``` 

### Structure of an app

1. `__init__.py` : This tells the interpreter that this directory is not a simple folder its a python package.

2. `admin.py` : This is used to display our models in the Django admin panel. This is where basic CRUD operations happen.

3.  `apps.py` : This file is created to help user to add any application level configuration for the app.

4. `models.py` : This file contains the essential fields and behaviors of the data that you are storing in the DB.

5.  `tests.py` : This file is used to run any tests in your Django project.

6.  `views.py` : In this file we create business logic of a specific app.