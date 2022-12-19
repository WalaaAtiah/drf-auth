 # LAB - Class 28

## Project: Authentication & Production Server

### Author: Walaa' Atiyh

### databass `sqlite3`

#### How to initialize/run your application (where applicable)
   
1. **Create the venv and activate it.**

    `python3.10 -m venv .venv`
    `source .venv/bin/activate`

2. **Installing Django.**

    \
   1. `pip install django`
   2. `pip install djangorestframework`
   3. `pip install djangorestframework-simplejwt`
   4. `pip install psycopg2-binary`
   5. `pip install whitenoise`
   6. `pip install  gunicorn`
   
   or 

   **install  requirements.txt**
   
   `pip3 install -r requirements.txt`

9. **To update the database**

    `python manage.py migrate`

10. **To run the server**

    `python manage.py runserver`

11. **To create an admin user**

    `python manage.py createsuperuser`

12. the admin username in the servers :admin
                 email:admin@admin.com
                 passward :admin1212


##  work with  docker 
  1.  `docker-compose up --build`
  2.   `docker-compose run web python manage.py migrate`
  3.  `docker-compose run web python manage.py createsuperuser`
   
  4.  the admin 
          
          username :admin
                email:admin@admin.com
                passward :admin1212
   5. the normal 
           
            username :normal
            passward :normal121212
            
  5. the staff 
   
             username :staff
             passward :staff1212


## Use Postman : Steps to manually test

**By using access token and refresh token :**
1. get the access tokenand refresh token from server
    * Use http://127.0.0.1:8000/api/token/ with post method from  Authorization select type: Bearer auth and inside body put UserName and password using JSON format for example:
   
   <img src="image/postman get access.png" alt="drawing" style="width:700px;"/>

    * **access token and refresh token**
```
      {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MTU3NTA3OCwiaWF0IjoxNjcxNDg4Njc4LCJqdGkiOiI4OTkyMjI4YThlMmU0MGJiYjYxYWI2NDM1YzdkYjc2ZiIsInVzZXJfaWQiOjEsInVzZXJuYW1lIjoiYWRtaW4ifQ.Hmb93JRRD9q7oW0izotcJHgsQF3o4U_AKp50BMXh03g",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcxNDg4OTc4LCJpYXQiOjE2NzE0ODg2NzgsImp0aSI6ImNlYTM4OGViZThiYTRhMzlhYjRmMWRmMGM1YWUxZTQxIiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJhZG1pbiJ9.AGLgu5CtHLT642nFjzjtpTCwiAu3DtoOrbj9BQ3Ss3A"
}
```

2.  **get a new access token :**
   
* Use http://127.0.0.1:8000/api/token/refresh/ with post method from  Authorization select type: Bearer auth and inside body put refresh token using JSON format for example:
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MTU3NTA3OCwiaWF0IjoxNjcxNDg4Njc4LCJqdGkiOiI4OTkyMjI4YThlMmU0MGJiYjYxYWI2NDM1YzdkYjc2ZiIsInVzZXJfaWQiOjEsInVzZXJuYW1lIjoiYWRtaW4ifQ.Hmb93JRRD9q7oW0izotcJHgsQF3o4U_AKp50BMXh03g"

* **you will get a new access token as response for example:**
  
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcxMzk2MzczLCJpYXQiOjE2NzEzOTU1MDYsImp0aSI6IjcyODQ1NjY0YzEwNTRjOGI5YTY0YjMxODdmZmRmNzE0IiwidXNlcl9pZCI6MX0.CFDFlyFbE9AvUsxTbAvdK6TNV5S8GB2_0LDNQpogBCE"

### git the list of the Move List  
   
   `http://127.0.0.1:8000/api/v1/movis/`






## [pull requests](https://github.com/WalaaAtiah/drf-auth/pull/1)
