- install Djano bitnami Stack

        django-admin createproject django_mysql_existing_db

        python3 manage.py startapp bazingaApp

- edit settings.py with:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'clinica',
            'HOST': '/Applications/djangostack-1.9.7-0/mysql/tmp/mysql.sock',
            'PORT': '3306',
            'USER': 'root',
            'PASSWORD': 'bazinga'
        }
    }

- add `bazingaApp` to INSTALLED_APPS:

        INSTALLED_APPS = [
            '...'
            'bazingaApp.apps.BazingaAppConfig',
        ]

        /Applications/djangostack-1.9.7-0/python/bin/python2.7 manage.py inspectdb

        /Applications/djangostack-1.9.7-0/python/bin/python2.7 manage.py inspectdb > bazinga/models.py


- edit the file models.py and then:

      /Applications/djangostack-1.9.7-0/python/bin/python2.7 manage.py shell

interact with the db and be happy
