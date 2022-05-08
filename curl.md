# Registration
curl --location --request POST 'http://127.0.0.1:8000/register/' --header 'Content-Type: application/json' --data-raw '{
    "username": "test2",
    "password": "A@123456",
    "password2": "A@123456",
    "email": "test1@gmail.com",
    "first_name": "test1",
    "last_name": "test1"

}'

# Login
curl --location --request POST 'http://127.0.0.1:8000/login/' --header 'Content-Type: application/json' --data-raw '{
    "username": "test2",
    "password": "A@123456"
}'

# Refresh
curl --location --request POST 'http://127.0.0.1:8000/token/refresh/' --header 'Content-Type: application/json' --data-raw '{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MjYyNjIyNiwiaWF0IjoxNjUyMDIxNDI2LCJqdGkiOiJmOTg1MmFiMzMzMmY0Y2NlOGM0MWRhOGJiMDVhNzc2MyIsInVzZXJfaWQiOjR9.Sh6ZeOqRL5mw52oZidp3lYhn3fLw1LMq1Bp-3YStgIU"
}'

#  Create Note
curl --location --request POST 'http://127.0.0.1:8000/api/note' --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMDk5NzM5LCJpYXQiOjE2NTIwMTMzMzksImp0aSI6ImIwODI0MzU4Y2FiNzQ0NTY5MjYwMjcyMDdiMzI1NGU3IiwidXNlcl9pZCI6MX0.l0RX1cs4A8FSUrfmjzz-3au3RDnCH6jeJT7rEYVGseI' --header 'Content-Type: application/json' --data-raw '{
    "title": "Python developer",
    "body": "This is my first Django application",
    "tags": "ashu",
    "is_public": false,
    "is_deleted": false
}'

# Update Note
curl --location --request PUT 'http://127.0.0.1:8000/api/note/1' --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMDk5NzM5LCJpYXQiOjE2NTIwMTMzMzksImp0aSI6ImIwODI0MzU4Y2FiNzQ0NTY5MjYwMjcyMDdiMzI1NGU3IiwidXNlcl9pZCI6MX0.l0RX1cs4A8FSUrfmjzz-3au3RDnCH6jeJT7rEYVGseI' --header 'Content-Type: application/json' --data-raw '{
    "title": "Python developer",
    "body": "This is my first Django application",
    "tags": "ashu",
    "is_public": false,
    "is_deleted": false
}'

# Delete Note
curl --location --request DELETE 'http://127.0.0.1:8000/api/note/11' --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMDk5NzM5LCJpYXQiOjE2NTIwMTMzMzksImp0aSI6ImIwODI0MzU4Y2FiNzQ0NTY5MjYwMjcyMDdiMzI1NGU3IiwidXNlcl9pZCI6MX0.l0RX1cs4A8FSUrfmjzz-3au3RDnCH6jeJT7rEYVGseI' --data-raw ''

# Filter Note
curl --location --request GET 'http://127.0.0.1:8000/api/filternotes/ashu' --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMDk5NzM5LCJpYXQiOjE2NTIwMTMzMzksImp0aSI6ImIwODI0MzU4Y2FiNzQ0NTY5MjYwMjcyMDdiMzI1NGU3IiwidXNlcl9pZCI6MX0.l0RX1cs4A8FSUrfmjzz-3au3RDnCH6jeJT7rEYVGseI' --header 'Content-Type: application/json' --data-raw '{
    "title": "Public Ashu",
    "body": "This is my first Ashu",
    "tags": "ashu",
    "is_public": false
}'

# Search Note
curl --location --request GET 'http://127.0.0.1:8000/api/searchnotes/ashu' --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMDk5NzM5LCJpYXQiOjE2NTIwMTMzMzksImp0aSI6ImIwODI0MzU4Y2FiNzQ0NTY5MjYwMjcyMDdiMzI1NGU3IiwidXNlcl9pZCI6MX0.l0RX1cs4A8FSUrfmjzz-3au3RDnCH6jeJT7rEYVGseI' --header 'Content-Type: application/json' --data-raw '{
    "title": "Public Ashu",
    "body": "This is my first Ashu",
    "tags": "ashu",
    "is_public": false
}'

# List Notes
curl --location --request GET 'http://127.0.0.1:8000/api/listnotes' --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMDk5NzM5LCJpYXQiOjE2NTIwMTMzMzksImp0aSI6ImIwODI0MzU4Y2FiNzQ0NTY5MjYwMjcyMDdiMzI1NGU3IiwidXNlcl9pZCI6MX0.l0RX1cs4A8FSUrfmjzz-3au3RDnCH6jeJT7rEYVGseI' --header 'Content-Type: application/json' --data-raw '{
    "title": "Public Ashu",
    "body": "This is my first Ashu",
    "tags": "ashu",
    "is_public": false
}'
