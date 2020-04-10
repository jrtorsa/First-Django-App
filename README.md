# First-Django-App
<b>My first Django app.</b><br> 
<br>
<b>Setting up the environment:</b><br>
<br>
You need to create a virtual environment in order to run the most updated version of Django.
Follow this steps.

<b>#to get the most recent version of pip.</b><br>
 python3 -m pip install --upgrade pip

<b>#to locate where is the virtual env.</b><br>
 which virtualenv

<b>#to locate the folder of your current version of pyhton.</b><br>
 which python3

 Access the folder in which you want to run the virtual env.

 virtualenv -p /usr/local/bin/python3 venv

<b>#this command inits the virtual env.</b><br>
 source venv/bin/activate

<b>#Checking the python version</b><br>
 python -V 

<b>#Deactiviting your virtual env.</b><br>
 deactivate 

<b>#If you want to delete your virtual env.</b><br>
 rm -rf venv

<b>Setting up Django.</b><br>

<b> I GUESS you have to pip install django for everytime you do it in a virtual env.</b><br>
Try - python -m django --version - just to check.
type - django-admin - You will see for the subcommands.

<b>To start a project.</b><br>

- django-admin startproject 'name of project'
Important! Access the folder of your projecto, then run:
- python3 manage.py runserver
