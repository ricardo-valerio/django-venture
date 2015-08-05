# django-admin commands:

    Type 'django-admin help <subcommand>' for help on a specific subcommand.

    Available subcommands:

    [django]
        check:

> Checks the entire Django project for potential problems.

        compilemessages:

> Compiles .po files to .mo files for use with builtin gettext support.

        createcachetable

> Creates the tables needed to use the SQL cache backend.

        dbshell

> Runs the command-line client for specified database, or the default database
if none is provided.

        diffsettings

> Displays differences between the current settings.py and Django's default
settings. Settings that don't appear in the defaults are followed by "###".

        dumpdata

> Output the contents of the database as a fixture of the given format (using
each model's default manager unless --all is specified).

        flush

> Removes ALL DATA from the database, including data added during migrations.
Unmigrated apps will also have their initial_data fixture reloaded. Does not
achieve a "fresh install" state.

        inspectdb

> Introspects the database tables in the given database and outputs a Django
model module.

        loaddata

> Installs the named fixture(s) in the database.

        makemessages

> Runs over the entire source tree of the current directory and pulls out all
strings marked for translation. It creates (or updates) a message file in the
conf/locale (in the django tree) or locale (for projects and applications)
directory. You must run this command with one of either the --locale,
--exclude or --all options.

        makemigrations

> Creates new migration(s) for apps.

        migrate

> Updates database schema. Manages both apps with migrations and those without.

        runfcgi

> Runs this project as a FastCGI application. Requires flup.

        runserver

> Starts a lightweight Web server for development.

        shell

> Runs a Python interactive interpreter. Tries to use IPython or bpython, if one
of them is available.

        showmigrations

> Shows all available migrations for the current project.

        sql

> Prints the CREATE TABLE SQL statements for the given app name(s).

        sqlall

> Prints the CREATE TABLE, custom SQL and CREATE INDEX SQL statements for the
given model module name(s).

        sqlclear

> Prints the DROP TABLE SQL statements for the given app name(s).

        sqlcustom

> Prints the custom table modifying SQL statements for the given app name(s).

        sqldropindexes

> Prints the DROP INDEX SQL statements for the given model module name(s).

        sqlflush

> Returns a list of the SQL statements required to return all tables in the
database to the state they were in just after they were installed.

        sqlindexes

> Prints the CREATE INDEX SQL statements for the given model module name(s).

        sqlmigrate

> Prints the SQL statements for the named migration.

        sqlsequencereset

> Prints the SQL statements for resetting sequences for the given app name(s).

        squashmigrations

> Squashes an existing set of migrations (from first until specified) into a
single new one.

        startapp

> Creates a Django app directory structure for the given app name in the current
directory or optionally in the given directory.

        startproject

> Creates a Django project directory structure for the given project name in the
current directory or optionally in the given directory.

        syncdb

> Deprecated - use 'migrate' instead.

        test

> Discover and run tests in the specified modules or the current directory.

        testserver

> Runs a development server with data from the given fixture(s).

        validate

> Deprecated. Use "check" command instead. Checks the entire Django project for
potential problems.
