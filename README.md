# First-Django-App
<b>My first Django app.</b><br> 
<br>
<b>Setting up the environment:</b><br>
<br>
You need to create a virtual environment in order to run the most updated version of Django.
Follow this steps.

<b>#to get the most recent version of pip.</b><br>
1. python3 -m pip install --upgrade pip

#to locate where is the virtual env.
2. which virtualenv

#to locate the folder of your current version of pyhton.
3. which python3

4. Access the folder in which you want to run the virtual env.

5. virtualenv -p /usr/local/bin/python3 venv

#this command inits the virtual env.
6. source venv/bin/activate

#Checking the python version
7.python -V 

#Deactiviting your virtual env.
8. deactivate 

#If you want to delete your virtual env.
9. rm -rf venv

Setting up Django.

<b> I GUESS you have to pip install django for everytime you do it in a virtual env.</b><br>
Try - python -m django --version - just to check.
type - django-admin - You will see for the subcommands.
<b>To start a project.</b><br>

- django-admin startproject 'name of project'
Important! Access the folder of your projecto, then run:
- python3 manage.py runserver
