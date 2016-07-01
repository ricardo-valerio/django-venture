    django-admin startproject django_sqlite_existing_db

    python3 manage.py startapp bazinga


    INSTALLED_APPS = [
        '...'
        'bazinga.apps.BazingaConfig',
    ]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            'NAME': os.path.join(BASE_DIR, 'bazinga.sqlite'),
        }
    }


paste some database (sqlite3 type) inside the project

    python3 manage.py inspectdb

    python3 manage.py inspectdb > bazinga/models.py

    python3 manage.py shell
