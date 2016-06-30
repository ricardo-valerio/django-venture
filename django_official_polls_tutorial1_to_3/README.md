### 1st step (create files):
    django-admin startproject django_official_polls_tutorial
    python3 manage.py startapp polls

### 2nd step (just to make sure the app is good to go):
    python3 manage.py runserver (CTRL + C to stop it)
    python manage.py runserver 0.0.0.0:8000
    python manage.py runserver 8080

### 3rd step (create super-user and tables of pre-existing apps):
    python3 manage.py createsuperuser   ( user:admin|pass:superuser )
    python manage.py migrate  (to create the database tables of the default apps)

### 4th step:
create some models and then:

    python3 manage.py makemigrations <desired-name-of-migration>
    python3 manage.py migrate

Note:

    python3 manage.py sqlmigrate <previous-desired-name-of-migration> <migration-number>   (shows underwood sql commands)

***Understanding the Workflow:***

- Change the models (inside an app's models.py)
- Run `python manage.py makemigrations` to create migrations for those changes
- Run `python manage.py migrate` to apply those changes to the database.

### 5th step (understanding the workflow):
    python3 manage.py shell   ( useful to explore the database API and interact with models on the fly )

### 6th step (create useful views that interact with models and return data to templates )
