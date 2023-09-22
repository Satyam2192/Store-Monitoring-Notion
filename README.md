# Store-Monitoring

##This repository contains the code for a Django-based API that provides various endpoints for managing timezones, store status, business hours, and generating reports.

Installation:

To run this project, you need to have Django and Django REST framework installed. You can install them using the following command:
clone the project
->git clone {Repo Link}
->pip install django djangorestframework

To insert data into database use command:
->python manage.py import_data
->python manage.py runserver

Database Setup:

Before running the project, you need to create the necessary database tables. Run the following commands to perform the database migrations:
->python manage.py makemigrations
->python manage.py migrate

Usage
To start the development server, use the following command:
->python manage.py runserver
Once the server is running, you can access the API endpoints using the following URLs:

Timezones: http://localhost:8000/api/v1/timezones

Store Status: http://localhost:8000/api/v1/store_status

Business Hours: http://localhost:8000/api/v1/business_hours

Trigger Report: http://localhost:8000/api/v1/trigger_report/

Get Reports: http://localhost:8000/api/v1/get-report/

Get Report Detail: http://localhost:8000/api/v1/get-report/{report_id}/
