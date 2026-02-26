
Django gives you some default database tables to manage the admin panel, authentication sessions and other Django related stuffs. So, those tables need to be created in the database before you create your own data. Simply run this `python manage.py migrate` command to get the database tables created. 

We get built-in admin panel where we can do almost all types of CRUD operations. To access the admin panel go to the `urls.py` -> `path('admin/', admin.site.urls)`

In the browser go to `admin/`, you'll see a page asking for login. To get the login credentials you need to create superuser. 

#### To create superuser:
	`python manage.py createsuperuser`

Give username(djangoadmin), email(work-email), password(laptop).

Run the server again and log in. You'll see the back-end of your Django website.


*Note: Each Django project has its own database. Your old project’s superuser does NOT exist in your new project’s database.*