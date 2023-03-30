# Django - Blog
Blog app based on Django framework, running: http://blog.sjgo.online


# Docker
- build `docker build -t test -f ./bin/Dockerfile .`
- run `docker run -it -p 8080:8080 -e PG_CONN='blog user pass 139.196.1.1 5432' test`
- Product server: Nginx serve static files and proxy requests to web server;  
Gunicorn handle server requests
- Function compute server: django develop server

# Django
## develop
https://docs.djangoproject.com/en/4.1/intro/tutorial01/
```
`django-admin startproject site`
`python manage.py startapp comment`
set up the database, create your first model, 
and get a quick introduction to Django’s automatically-generated admin site
https://docs.djangoproject.com/en/4.1/intro/tutorial02/
```
## db migration
```
- By running makemigrations, you’re telling Django that you’ve made some changes to your models
`python manage.py makemigrations blog`
- The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables
`python manage.py migrate`
- Creating an admin user
First we’ll need to create a user who can login to the admin site. Run the following command:
http://127.0.0.1:8000/admin/; admin/admin123; 
`python manage.py createsuperuser`
```
## upgrade-version
https://docs.djangoproject.com/en/4.1/howto/upgrade-version
`python -Wa manage.py test`
## Static files (CSS, JavaScript, Images)
https://docs.djangoproject.com/en/3.2/howto/static-files/
`python manage.py collectstatic`

# Poetry
https://python-poetry.org/docs/cli/#init
poetry init
poetry shell
 