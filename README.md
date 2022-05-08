# Backend Coding Challenge

[![Build Status](https://github.com/Thermondo/backend-code-challenge/actions/workflows/main.yml/badge.svg?event=push)](https://github.com/Thermondo/backend-code-challenge/actions)

Backend REST API for a simple note-taking app.


### Application Features:
* Users can add, delete and modify their notes using django mixins
* Users must be logged in, in order to view/add/delete/etc. their notes using default django 'isauthenticated' and custom made 'isowner' permissions
* Notes can be either public or private - Public notes can be viewed without authentication, however they cannot be modified
* Users can see a list of all their notes using django apiview
* Users can filter their notes via tags
* Search contents of their notes with keywords
* User management API to create new users using default admin panel
* Token based authentication using third party package djangorestframework-simplejwt supported by django

### The model fields:
* id - pk
* title, body, tags - represents notes details
* is_public - represents whether notes made by user is public or private
* is_deleted - represents the deleted entry. This is for soft delete
* owner - represents the creater of the note

### Project Setup
* cd to root folder and run following commands
* sudo pip3 install virtualenv
* virtualenv venv
* pip3 install -r requirements.txt
* python3 manage.py makemigration
* python3 manage.py migrate
* python manage.py runserver

### Access APIs
* The following application can be access via postman. Collection present at root location as Thermondo.postman_collection.json 
* Or You may look use the Curl Requests mentioned in curl.md file 
