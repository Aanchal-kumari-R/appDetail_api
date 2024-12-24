# APP MANAGEMENT API 
This project is a Python-based RESTFUL API using Django. The API allow you to manage app details, including adding, retrieving, and deleting app information. 
This application uses a SQLite database for storing app details. 

# FEATURES 
POST /add-app: Add app details to the database 
GET /get-app/{id}: Retrieve app details by ID
DELETE /delete-app/{id}: Delete an app by ID  

# PREREQUISITES 
Before setting up the project , ensure you have the following installed on your system. 
Python 3.12.2 
Django 5.0.7 
SQLite (default) 

# SetUp Instructions 
1) Create and active virtual Environment in the appdetails folder using this command
pip install virtualenv 
python -m venv myenv 

2)install Django Rest Framework usign this command 
pip install djangorestframework   

3) Create project name using this command
   django-admin startproject mysite
   naviage to project name
   cd mysite in cmd
   
5) Run the project using this command to check the project is running or not.
   python manage.py runserver
   
6) Create app name using this command
   python manage.py startapp appinfo

7) Add app name and rest_framework in the setting.py in project
   INSTALLED_APPS = [
       ...
      'rest_framework',
      'appinfo'.
     ]

8) After creating models run Migrations
   Python manage.py makemigrations
   python manage.py migrate

9) Create SuperUser
    python manage.py createsuperuser
    username - aanchalsingh
    email - aanchalkumari096@gmail.com
    password - aanchal123
   
10) Run the Server
   python manage.py runserver
   Access the API at http://127.0.0.1:8000.

# API Endpoints
1. Add App
 * URL: /add-app
 * Method: POST
   
2. Get App Details
URL: /get-app/{id}
Method: GET
Response:
{
  "id": 1,
  "app_name": "Example App",
  "version": "1.0.0",
  "description": "This is a sample app."
}

3. Delete App
URL: /delete-app/{id}
Method: DELETE
Response:
json
Copy code
{
  "message": "App deleted successfully!"
} 

3) Test the Api using curl and Postman 


  


