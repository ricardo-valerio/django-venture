### manage.py commands:

    Type 'manage.py help <subcommand>' for help on a specific subcommand.

    Available subcommands:

    [auth]
        changepassword

> Change a user's password for django.contrib.auth.

        createsuperuser

> Used to create a superuser.

# see file `django-admin-commands.md`

    [django]
        check
        compilemessages
        createcachetable
        dbshell
        diffsettings
        dumpdata
        flush
        inspectdb
        loaddata
        makemessages
        makemigrations
        migrate
        runfcgi
        shell
        showmigrations
        sql
        sqlall
        sqlclear
        sqlcustom
        sqldropindexes
        sqlflush
        sqlindexes
        sqlmigrate
        sqlsequencereset
        squashmigrations
        startapp
        startproject
        syncdb
        test
        testserver
        validate


    [sessions]
        clearsessions

> Can be run as a cronjob or directly to clean out expired sessions (only with
the database backend at the moment).

    [staticfiles]
        collectstatic

> Collect static files in a single location.

        findstatic

> Finds the absolute paths for the given static file(s).

        runserver

> Starts a lightweight Web server for development and also serves static files.

