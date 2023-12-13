# Meryem

used (https://www.logoai.com/) to create logo

https://www.logoai.com/download?logo=748114


## Python and Django

apt-get install python3-venv
virtualenv -p python3 .venv
python3 -m venv .venv
source ./.venv/bin/activate
python3 -m pip install django
python3 -m pip install pip
python3 -m pip install djlint
python3 -m pip install django-debug-toolbar
python3 -m pip install pytest-django
python3 -m pip install --upgrade django
python3 -m pip install --upgrade pip

django-admin startproject config . 
python3 manage.py startapp website 
python3 manage.py makemigrations
python3 manage.py migrate 
python3 manage.py createsuperuser
pip freeze > requirements.txt 
python3 manage.py runserver 0.0.0.0:8000


## troubleshooting
python manage.py makemigrations website --empty
python3 manage.py makemigrations
python3 manage.py migrate 





## Other tutorials
admin: 
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site

Python Django Dentist Website #4
(https://www.youtube.com/watch?v=cUaZ0ElJ760)

(https://dockerize.io/guides/python-django-guide)

(https://www.youtube.com/watch?v=nWBgg2QXtSA)

## start local smtp server - atviavate virtual env first
(https://docs.djangoproject.com/en/4.2/topics/email/)

use a “dumb” SMTP server that receives the emails locally and displays them to the terminal, but does not actually send anything
python -m pip install aiosmtpd
python -m aiosmtpd -n -l localhost:8025

python -m smtpd -n -c DebuggingServer localhost:1025

## Read other Stuffs:
### django enviromental passsword

python -m pip install argon2-cffi

### Creating Environment Variables
(https://djangocentral.com/environment-variables-in-django/)

pip install django-environ

### Django send email
https://www.sitepoint.com/django-send-email/
https://steelkiwi.com/blog/sending-emails-in-django-definitive-tutorial/
https://www.abstractapi.com/guides/django-send-email

### SSL ‘Certificate_Verify_Failed’ Error
pip install --upgrade certifi

### Create createsuperuser automation
https://stackoverflow.com/questions/6244382/how-to-automate-createsuperuser-on-django#26091252

### python dictionaries



## Production hosting online

pip install gunicorn
pip install django-heroku
pip install dj_database_url
pip install python-decouple
touch Procfile
