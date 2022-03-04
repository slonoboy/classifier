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
Todo app allows you to create your own account where your tasks will be saved. Go to /registration, fill the fields and submit the form.
![reg](https://user-images.githubusercontent.com/52863393/150379000-cb51e15f-a443-4069-a1ab-73d3912a394c.png)
Then you can use an account to log in via login form on /login route
![login](https://user-images.githubusercontent.com/52863393/150378998-26c2f1fc-8c3a-47ce-bb86-919f662fe693.png)
By default you have no tasks an fresh account and the main page will look like this
![index_no_tasks](https://user-images.githubusercontent.com/52863393/150378994-c2a84af1-5957-43ee-883a-d456db0b514c.png)
Try to add a task you want to complete
![index_one_tasks](https://user-images.githubusercontent.com/52863393/150378996-5f4f17a1-b8e4-4ada-988a-0a9a3e872f36.png)
When the task is completed you can push 'complete' button and the task will move to 'completed' tasks. Also if you want to delete a task just push the button 'delete'
![index](https://user-images.githubusercontent.com/52863393/150378988-98c2bd98-2468-47a4-b339-85989336121c.png)




