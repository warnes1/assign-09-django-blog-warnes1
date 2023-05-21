Repository name: https://github.com/warnes1/07-django-blog-warnes1

(djangoenv)$ pip install Django==3.1.5
  Collecting Django
    Downloading Django-2.1.1-py2.py3-none-any.whl (6.9MB)
      100% |████████████████████████████████| 6.9MB 47kB/s
  Installing collected packages: Django
  Successfully installed django-2.1.1
(djangobenv)$

====== Then we started the `mysite` project and initialized our database:======

(djangoenv)$ django-admin startproject mysite
(djangoenv)$ cd mysite
(djangoenv)$ python manage.py runserver        # Load http://localhost:8000 and then shut the server
                                               # down with CTRL-C when you're done looking at the
                                               # welcome page.
(djangoenv)$ python manage.py migrate
(djangoenv)$ python manage.py createsuperuser  # Use `winpty python manage.py createsuperuser` if
                                               # on Windows GitBash
====== Finally, we created the `polling` app.======


(djangoenv)$ python manage.py startapp polling # Then add `polling` to INSTALLED_APPS in
                                               # mysite/settings.py