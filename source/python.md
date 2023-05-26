# Python

## Links

- [Force Restart Faild Gunicor Service](https://unix.stackexchange.com/questions/513972/how-to-fix-start-limit-hit-trying-to-start-gunicorn-on-ubuntu-18#answer-552135)
- [Django-Rules - Awesome Django Authorization, Without The Database](https://github.com/dfunckt/django-rules)
- [Github - Pydanny/Cookiecutter-Django: Cookiecutter Django Is A Framework For Jumpstarting Production-Ready Django Projects Quickly.](https://github.com/pydanny/cookiecutter-django)
- [Custom Permission_Classes For Default Django Rest Framework Methods](https://stackoverflow.com/questions/35970970/django-rest-framework-permission-classes-of-viewset-method)
- [Django3 Language Code Error](https://stackoverflow.com/questions/59156630/translation-e004-you-have-provided-a-value-for-the-language-code-setting-that-i#answer-59157763)
- [Revert The Last Migration](https://stackoverflow.com/questions/32123477/how-to-revert-the-last-migration#answer-32124113)
- [Reverse Many2Many Inline Admin](https://stackoverflow.com/questions/10904848/adding-inline-many-to-many-objects-in-django-admin)
- [Language_Code Not Working](https://stackoverflow.com/questions/47063007/django-language-code-en-but-displays-fr#answer-47063904)
- [Resources Translated To Persian (Iran)](https://www.transifex.com/open-edx/dashboard/all_resources/fa_IR/?project=open-edx-releases#1/?o=perc&d=desc)
- [Django Python Support](https://docs.djangoproject.com/en/3.0/faq/install/#what-python-version-can-i-use-with-django)
- [Add A Value Sensitive Unique Together Constraint](https://stackoverflow.com/questions/16474552/is-there-any-more-elegant-way-to-add-a-value-sensitive-unique-together-constrain#answer-59939626)
- [Drf Write_Only_Fields](https://stackoverflow.com/questions/34989915/write-only-read-only-fields-in-django-rest-framework#answer-36771366)
- [Get Translated Choice In Drf](https://stackoverflow.com/questions/62045788/drf-serializer-return-translated-choice-field-value/62062034#62062034)
- [All Language Codes](http://www.i18nguy.com/unicode/language-identifiers.html)
- [Mongosql - Lets You Query Sqlalchemy Like A Mongodb Database](https://pypi.org/project/mongosql/)
- [Microsoft Visual C++ 14.0 Is Required](https://stackoverflow.com/questions/44951456/pip-error-microsoft-visual-c-14-0-is-required?rq=1/#answer-44953739)
- [Locale Error: Unsupported Locale Setting](https://stackoverflow.com/questions/14547631/python-locale-error-unsupported-locale-setting#answer-14548156)
- [Locale Problem In Docker](https://serverfault.com/questions/54591/how-to-install-change-locale-on-debian#answer-894545)
- [Celery Timezones Types](https://stackoverflow.com/questions/13866926/is-there-a-list-of-pytz-timezones)
- [Python Dates Types](https://www.w3schools.com/python/python_datetime.asp)
- [Convert Python File To .Exe](https://m.youtube.com/watch?feature=youtu.be&v=UZX5kH72Yx4)
- [Get The Filepath For A Class](https://stackoverflow.com/questions/697320/how-do-i-get-the-filepath-for-a-class-in-python/697395#697395)
- [All File Open Modes](https://stackoverflow.com/questions/6648493/how-to-open-a-file-for-both-reading-and-writing/58925279#58925279)
- [Time Complexity (Big O)](https://wiki.python.org/moin/TimeComplexity)
- [Number of Gunicorn workers in Kubernetes](https://forum.djangoproject.com/t/gunicorn-workers-in-kubernetes/7918/2)

## Get All Import Able Modules And Packages

```
import pkgutil
search_path = ['.'] # set to None to see all modules importable from sys.path
all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
print(all_modules)
```

## Celery

Install:

- celery: `pip install celery`
- celery and redis for broker `pip install -U "celery[redis]"`

usage:

```python
# celery_config.py

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
# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
CELERY_APP = Celery('<app name: karestoon>')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
CELERY_APP.config_from_object('<celery_config.py address>', namespace='CELERY')

# Load task modules from all registered Django app configs.
CELERY_APP.autodiscover_tasks()


# sample task
@CELERY_APP.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
    
```

commands:

- kill celery process:

  `kill -9 $(ps aux | grep celery | grep -v grep | awk '{print $2}' | tr '\n' ' ') > /dev/null 2>&1`

- view worker logs: `celery -A <worker name: karestoon> worker --loglevel=info`

## Sphinx

install and start:

1. `pip install sphinx`

2. ```
   mkdir docs
   cd docs
   sphinx-quickstart
   ```

commands:

tip: run commands in `docs` directory

- build dist version of documentation: `make html`
- remove dist version: `make clean`

commands source page: <https://www.sphinx-doc.org/en/master/man/sphinx-build.html>

### Theming

#### Read The Docs Theme

 `pip install sphinx_rtd_theme`

```python
# conf.py

html_theme = 'sphinx_rtd_theme'
html_theme_path = ['_templates',]
```

#### Custom Style

add `extra.css` in `_static/css` directory

```python
# conf.py

def setup(app):
    app.add_stylesheet('css/extra.css')
```

### Extensions

#### Autodoc

```python
# conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

extensions = ['sphinx.ext.autodoc']
```

##### Autodoc Sample Usage

```rst
.. automodule:: <python file path: apps.core.models.user>
   :members:
   :undoc-members:
   :show-inheritance:
```

#### Other Doctype Support

```python
# conf.py

extensions = ['sphinx.ext.napoleon']

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
```

#### Markdown Support

`pip install recommonmark`

```python
# conf.py

extensions = ['recommonmark']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
```

#### Markdown Table Support

`pip install sphinx-markdown-tables`

```python
# conf.py

extensions = ['sphinx_markdown_tables']
```

