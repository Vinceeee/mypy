# markdown for django

- create project
django-admin startproject <project-name> 

- create app
django-admin startapp <app-name>

- make db migrate , use to update database
./manager.py makemigrations <app-name>

- update sql 
./manager.py sqlmigrate <app-name> <migrate-seq>

- commit db migrate
./manager.py migrate 
