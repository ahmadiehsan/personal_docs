# Django

## postgres

`sudo apt install postgresql`

```python
# settings.py

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

## redis

`sudo apt install redis-server`

`pip install django-redis`

```python
# settings.py

# Redis
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

## memcached

`sudo apt install memcached`

`pip install python-memcached`

``` python
# settings.py

# Memcached
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
```

## cache

first add memcached or redis as cache database to django settings.py

- in template

  ```python
  {% load cache %}
  
  {% cache 500 <cache name> %}
  	...
  {% endcache %}
  ```

- in url

  ```python
  from django.views.decorators.cache import cache_page
  
  urlpatterns = [
      path('foo/<int:code>/', cache_page(60 * 15)(<cache name>)),
  ]
  ```

- in view

  ```python
  from django.views.decorators.cache import cache_page
  
  @cache_page(60 * 15)
  def my_view(request):
      ...
  ```

- custom

  ```python
  from django.core.cache import cache
  
  # set
  cache.set('<key>', '<value>', <timeout: second>)
  
  # get
  cache.get('<key>')
  ```

## password hashing

`pip install bcrypt django[argon2]`

```python
# settings.py
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]
```

## internationalization (i18n)

```python
# settings.py
# Internationalization (i18n)
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)
```

commands:

- Creating language and collect messages (.po):

  `django-admin makemessages -l <lankuage code: fa_IR>`

- Update exist languages messages (.po):

  `django-admin makemessages -a`

- Convert .po file to .mo:

  `django-admin compilemessages`

## celery

```python
# settings.py

# config variables must start with "namespace" in .config_from_object function
# for example: CELERY_

CELERY_IMPORTS = ('apps.job.tasks',)  # task files address
CELERY_BROKER_URL = 'redis://localhost:6379/'  # redis as broker
CELERY_RESULT_BACKEND = 'redis://localhost:6379/'  # redis as small db
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'pickle'  # default: 'json'
CELERY_RESULT_SERIALIZER = 'pickle'  # default: 'json'
CELERY_TIMEZONE = 'Asia/Tehran'
```

```python
# DJANGO_MAIN_APP/celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    '<django settings path: karestoon.settings.local>'
)

CELERY_APP = Celery('<app name: karestoon>')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
CELERY_APP.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
CELERY_APP.autodiscover_tasks()


# sample task
@CELERY_APP.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

```

## after start project checklist

```python
# settings.py

import datetime
import locale
import logging.config

os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DJANGO_APPS = []
PROJECT_APPS = []
INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS

'DIRS': [os.path.join(BASE_DIR, 'templates')], # Templates
    
LANGUAGE_CODE = 'fa-ir'  # django 2
LANGUAGE_CODE = 'fa'  # django 3
locale.setlocale(locale.LC_ALL, 'fa_IR')
TIME_ZONE = 'Asia/Tehran'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{name} {levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'fileDebug': {
            'class': 'logging.FileHandler',
            'filename': '/var/log/<project name: karestoon>/debug.log',
            'formatter': 'verbose',
            'level': 'DEBUG',
        },
        'fileError': {
            'class': 'logging.FileHandler',
            'filename': '/var/log/<project name: karestoon>/error.log',
            'formatter': 'verbose',
            'level': 'ERROR',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'level': 'WARNING',
        }
    },
    'loggers': {
        'suds': {
            'handlers': [],
            'propagate': True,
            'level': 'CRITICAL',
        },
        '': {
            'handlers': ['fileDebug', 'fileError', 'console'],
            'propagate': True,
            'level': 'DEBUG',
        },
    },
}
logging.config.dictConfig(LOGGING)
LOGGER_V1 = logging.getLogger(__name__)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_REDIRECT_URL = "/profile/"
LOGOUT_REDIRECT_URL = "/"

LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]

MIDDLEWARE = ['django.middleware.gzip.GZipMiddleware',]
```

```python
# urls.py

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

