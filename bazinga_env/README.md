# create virtual env
python3 -m venv bazinga_env

# activate virtual env
source bin/activate

# install django or other stuff
pip3 install django    # last version
pip3 install django==VERSION

# list all packages inside the env
pip3 freeze

# export the packages to a requirements.txt file
pip 3 freeze > requirements.txt

# install packages inside the requirements.txt file
pip3 install -r requirements.txt

# deactivate venv
deactivate
