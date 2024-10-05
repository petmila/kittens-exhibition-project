# kittens-exhibition-project

REST API for a kitten exhibition written with Django
----
### Quick Start
To get this project up and running locally on your computer:

1. Set up the Python development environment.
Assuming you have Python setup, run the following commands:
```
    pip install -r requirements.txt
    py manage.py makemigrations
    py manage.py migrate
    py manage.py test # Run the standard tests. These should all pass.
    py manage.py createsuperuser # Create a superuser
    py manage.py runserver
```
Документацию можно посмотреть по ссылке: http://127.0.0.1:8000/swagger/