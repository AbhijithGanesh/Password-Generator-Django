# Password Generator
This is the repository which contains deployment files of Heroku
There is a ProcFile which is required by the Heroku Platform for deployment.
The package requirements are given in the requirements.txt
The runtime.txt contains the python version which is essential for the heroku deployment
Heroku Link: https://team-unhackables.herokuapp.com/

# The idea behind this project
We have developed this project with the idea of creating strong,uncrackable passwords which can be used for secure-applications. The password is a 128-bit generated p  Password through a secure-pattern, this can be utilized as a template for future projects. 
The password is based on the random module and django, the project can be extended to 256-bit and/or 32-bit passphrases which can be used in its own secure domain. Any future updates are welcome, This is an adaptation of the Annual Computer Science Project deployed  by Abhijith G, Snehit K and Manikrishneshwar S. 


# How to run this server
Clone the project and extract it to your localsystem,
This will download the virtual-environment to run the django-project. If you want to create your own environment do the following:
  1. Delete CSPROJECT
  2. Open Terminal with this directory and run ```python -m venv <VirtualEnvName>```
  3. Then activate your virtual environment 
  4. Then Install Django using  ```pip install django```
  5. Once it is installed, run ```python manage.py runserver```
  This should run the server, if there are any errors saying ```ModuleNotFound``` Then ---> ```pip install <modulename>```
  

