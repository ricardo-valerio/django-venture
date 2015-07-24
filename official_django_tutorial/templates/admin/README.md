find the django template inside the source files:

	python3 -c "
		import sys
		sys.path = sys.path[1:]
		import django
		print(django.__path__)"


	/usr/local/lib/python3.4/dist-packages/Django-1.8.3-py3.4.egg/django

