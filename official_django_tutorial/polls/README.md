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


#####################################
# TUTORIAL PART 4
#####################################

A common case of basic Web development: getting data from the database 
according to a parameter passed in the URL, loading a template and returning 
the rendered template. Because this is so common, Django provides a shortcut, 
called the “generic views” system.

Generic views abstract common patterns to the point where you don’t even 
need to write Python code to write an app.

Let’s convert our poll app to use the generic views system, so we can 
delete a bunch of our own code. We’ll just have to take a few 
steps to make the conversion. We will:
   - Convert the URLconf.
   - Delete some of the old, unneeded views.
   - Introduce new views based on Django’s generic views.

#####################################
# TUTORIAL PART 5
#####################################

* Introducing automated testing:

Tests are simple routines that check the operation of your code.

Testing operates at different levels. Some tests might apply to a tiny detail (does a particular model method return values as expected?) while others examine the overall operation of the software (does a sequence of user inputs on the site produce the desired result?). That’s no different from the kind of testing you did earlier in Tutorial 1, using the shell to examine the behavior of a method, or running the application and entering data to check how it behaves.

What’s different in automated tests is that the testing work is done for you by the system. You create a set of tests once, and then as you make changes to your app, you can check that your code still works as you originally intended, without having to perform time consuming manual testing.


* Basic testing strategies:

There are many ways to approach writing tests.

Some programmers follow a discipline called “test-driven development”; they actually write their tests before they write their code. This might seem counter-intuitive, but in fact it’s similar to what most people will often do anyway: they describe a problem, then create some code to solve it. Test-driven development simply formalizes the problem in a Python test case.

More often, a newcomer to testing will create some code and later decide that it should have some tests. Perhaps it would have been better to write some tests earlier, but it’s never too late to get started.

Sometimes it’s difficult to figure out where to get started with writing tests. If you have written several thousand lines of Python, choosing something to test might not be easy. In such a case, it’s fruitful to write your first test the next time you make a change, either when you add a new feature or fix a bug.

So let’s do that right away.

* Running tests:

In the terminal, we can run our test:

     python3 manage.py test polls

As long as your tests are sensibly arranged, they won’t become unmanageable. Good rules-of-thumb include having:

   - a separate TestClass for each model or view
   - a separate test method for each set of conditions you want to test
   - test method names that describe their function
   
If you have a complex application, you may want to run tests automatically with every commit for the purposes of continuous integration, so that quality control is itself - at least partially - automated.

A good way to spot untested parts of your application is to check code coverage. This also helps identify fragile or even dead code. If you can’t test a piece of code, it usually means that code should be refactored or removed. Coverage will help to identify dead code.
