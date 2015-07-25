The first step in writing a database Web app in Django is to define your models
– essentially, your database layout, with additional metadata.


we’ll create two models: Question and Choice.

- A Question has a question and a publication date.
- A Choice has two fields: the text of the choice and a vote tally.
- Each Choice is associated with a Question.

These concepts are represented by simple Python classes.

-> go to the models.py file



#####################################
# TUTORIAL PART 2
#####################################

First we’ll need to create a user who can login to the admin site.
Run the following command:

####################################################################
# 	8- python3 manage.py createsuperuser
####################################################################

Enter your desired personal info that's prompted to you.

Username (leave blank to use 'zzz'): admin
Email address: admin@gmail.com
Password: ***** (admin)
Password (again): ***** (admin)
Superuser created successfully.

Since translation is turned on by default, the login screen may be displayed in your own language, depending on your browser’s settings and on whether Django has a translation for this language.

You should see a few types of editable content: groups and users. They are provided by django.contrib.auth, the authentication framework shipped by Django.

But where’s our poll app? It’s not displayed on the admin index page.

Just one thing to do: we need to tell the admin that Question objects have an admin interface. To do this, edit the polls/admin.py file.

#####################################
# TUTORIAL PART 3
#####################################

Write code inside the views.py file.
To call the view (action or method), we need to map it to a URL - and for this we need a URLconf.
To create a URLconf in the polls directory, create a file called urls.py. Your app directory should now look like:

polls/
    __init__.py
    admin.py
    models.py
    tests.py
    urls.py
    views.py

The next step is to point the root URLconf at the polls.urls module.
In mysite/urls.py insert an include(), leaving you with:

    url(r'^polls/', include(polls.urls))

