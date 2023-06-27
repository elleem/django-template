## A Django Template

Welcome to a Django Template with CRUD functionality. 

Authored by Lauren Main. 

### Features

- Django 4.2 and Python 3.11
- Install via pip
- User log in/out, sign up
- Styling with Flowbite and Tailwind
- Templates for create, read, update, and delete. 


Set up environment -

    python3.11 -m venv .venv
    source .venv/bin/activate

Setup -

    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    python -m pip install django-compressor