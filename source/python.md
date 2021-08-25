# Python

## Get all import able modules and packages

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

### theming

#### read the docs theme

 `pip install sphinx_rtd_theme`

```python
# conf.py

html_theme = 'sphinx_rtd_theme'
html_theme_path = ['_templates',]
```

#### custom style

add `extra.css` in `_static/css` directory

```python
# conf.py

def setup(app):
    app.add_stylesheet('css/extra.css')
```

### extensions

#### autodoc

```python
# conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

extensions = ['sphinx.ext.autodoc']
```

##### autodoc sample usage

```rst
.. automodule:: <python file path: apps.core.models.user>
   :members:
   :undoc-members:
   :show-inheritance:
```

#### other doctype support

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

#### markdown support

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

#### markdown table support

`pip install sphinx-markdown-tables`

```python
# conf.py

extensions = ['sphinx_markdown_tables']
```

