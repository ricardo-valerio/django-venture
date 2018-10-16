#!/usr/local/bin/python3

from termcolor import colored
import clipboard


VIRTUALENV_NAME           = input("Name for Virtual-Environment: ")
DJANGO_VERSION_TO_INSTALL = input("Django Version: ")
DJANGO_PROJECT_TO_CREATE  = input("Project Name: ")


amp = " &&"

# Note "WEBDEV-DJANGO" is just an alias I made in my .zshrc file:
# alias WEBDEV-DJANGO="cd ~/ABSOLUTE/PATH/TO/YOUR/DJANGO-PROJECTS-FOLDER"
command = "WEBDEV-DJANGO"
command += amp + f" python3 -m venv {VIRTUALENV_NAME}"
command += amp + f" cd {VIRTUALENV_NAME}"
command += amp + " source bin/activate"
command += amp + " pip3 install --upgrade pip"
command += amp + f" pip3 install Django=={DJANGO_VERSION_TO_INSTALL}"
command += amp + " pip3 freeze > requirements.txt"
command += amp + f" echo '- Django Version being used: {DJANGO_VERSION_TO_INSTALL}' >> README.md"
command += amp + " echo '- To activate the virtualenv just type <source bin/activate>' >> README.md"
command += amp + " echo '- To install the requirements type: <pip3 install -r requirements.txt>' >> README.md"
command += amp + " echo '- To deactivate the virtualenv just type <deactivate>' >> README.md"
command += amp + \
f" ./bin/django-admin startproject {DJANGO_PROJECT_TO_CREATE}__with_{DJANGO_VERSION_TO_INSTALL.replace('.','_')}"
command += amp + f" cd {DJANGO_PROJECT_TO_CREATE}__with_{DJANGO_VERSION_TO_INSTALL.replace('.', '_')}"

print("\n", command, "\n")

clipboard.copy(command)

print(colored("The", "red"), end=" ")
print(colored("command", "yellow"), end=" ")
print(colored("was", "blue"), end=" ")
print(colored("successfuly", "green"), end=" ")
print(colored("copied", "magenta"), end=" ")
print(colored("to", "cyan"), end=" ")
print(colored("the", "red"), end=" ")
print(colored("clipboard", "yellow"), end="")
print(colored("!", "blue"), "\n")
