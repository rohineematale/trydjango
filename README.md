# trydjango
Starting with Django framwork

Create Virtual Environment with python3 & Install Django:
1. Make sure you have python3 installed on system check using `python3 -V`.
2. Go to application folder and create virtual environment by using `virtualenv -p python3 app_shell`. This will create actiavation files in app_shell folder.
3. Install Django using `pip install django==2.0.7`

Migrations:
1. change field values in model.py
2. create migration using `python manage.py makemigration`
3. run migration using `python manage.py migrate`


Run server
1. activate environment by `source <app_shell>/bin/activate`
2. start server usin `python manage.py runserver`