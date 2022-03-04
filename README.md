# Django image classifier app
### Installation 
Download files to your project folder. Create virtual environment and use requirements to install required packages (you can use pip install -r /path/to/requirements.txt command).  Raise postgresql database server and change database configurations in setting.py. Change the following rows in settings.py:
``` python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<database name>',
        'USER': '<username>',
        'PASSWORD': '<user password>',
        'HOST': 'localhost',
        'PORT': '',
    }
}

```
###  Usage
Locate your command line location to folder with manage.py file and type python manage.py runserver. Now you can open web browser and connect to your local web server by typing http://127.0.0.1:8000/ in address bar. Here you can upload files and after submitting them a new page opens. On the new page you can see the results of all image classifications stored in the database.

You can interract with database by going to admin panel. But firstly your need to create super user. Type python manage.py createsuperuser. Now you have a super user who can use admin panel and edit database data.

### Examples
It is the main page. Upload files you want and click submit
![main](https://user-images.githubusercontent.com/52863393/156700934-35d47ae4-8bde-4c28-b483-eb1371d23f69.png)
After submitting, on the new page you can see the results or go back if you want to
![results](https://user-images.githubusercontent.com/52863393/156700937-481e4b59-78a6-4d8c-b72d-926715460da7.png)





