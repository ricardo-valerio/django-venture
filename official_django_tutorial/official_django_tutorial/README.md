/*********************************************************
*   1- django-admin startproject mysite
*********************************************************/

Let’s look at what startproject created:

mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py

These files are:

    The outer mysite/ root directory is just a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.

    manage.py:
        A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.

    The inner mysite/ directory
        is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).

    mysite/__init__.py:
        An empty file that tells Python that this directory should be considered a Python package. (Read more about packages in the official Python docs if you’re a Python beginner.)

    mysite/settings.py:
        Settings/configuration for this Django project. Django settings will tell you all about how settings work.

    mysite/urls.py:
        The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.

    mysite/wsgi.py:
        An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.



    Inside the settings.py file, some of the default applications (INSTALLED_APPS) make use of at least one database table, though, so we need to create the tables in the database before we can use them. To do that, run the following command:

/*********************************************************
*   2- python3 manage.py migrate
*********************************************************/

Operations to perform:
  Synchronize unmigrated apps: messages, staticfiles
  Apply all migrations: admin, contenttypes, sessions, auth
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying sessions.0001_initial... OK

/*********************************************************
*   3- python3 manage.py runserver
*********************************************************/

Performing system checks...

System check identified no issues (0 silenced).
July 23, 2015 - 11:42:21
Django version 1.8.3, using settings 'official_django_tutorial.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.



By default, the runserver command starts the development server on the internal IP at port 8000.

If you want to change the server’s port, pass it as a command-line argument. For instance, this command starts the server on port 8080:

    $ python3 manage.py runserver 8080

If you want to change the server’s IP, pass it along with the port. So to listen on all public IPs (useful if you want to show off your work on other computers on your network), use:

    $ python3 manage.py runserver 0.0.0.0:8000

Full docs for the development server can be found in the runserver reference.

You don’t need to restart the server for code changes to take effect. However, some actions like adding files don’t trigger a restart, so you’ll have to restart the server in these cases.




Projects vs. apps

What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a simple poll app. A project is a collection of configuration and apps for a particular Web site. A project can contain multiple apps. An app can be in multiple projects.

Your apps can live anywhere on your Python path. In this tutorial, we’ll create our poll app right next to your manage.py file so that it can be imported as its own top-level module.

To create your app, make sure you’re in the same directory as manage.py and type this command:

/*********************************************************
*   4- python3 manage.py startapp polls
*********************************************************/

That’ll create a directory polls, which is laid out like this:

polls/
    __init__.py
    admin.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py

This directory structure will house the poll application.

The first step in writing a database Web app in Django is to define your models – essentially, your database layout, with additional metadata.
