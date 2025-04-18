# Python

## Links

- [Force restart faild Gunicor service](https://unix.stackexchange.com/questions/513972/how-to-fix-start-limit-hit-trying-to-start-gunicorn-on-ubuntu-18#answer-552135)
- [Cookiecutter Django](https://github.com/pydanny/cookiecutter-django)
- [Django language codes](https://stackoverflow.com/questions/59156630/translation-e004-you-have-provided-a-value-for-the-language-code-setting-that-i#answer-59157763)
- [All language codes](http://www.i18nguy.com/unicode/language-identifiers.html)
- [Django reverse Many2Many inline admin](https://stackoverflow.com/questions/10904848/adding-inline-many-to-many-objects-in-django-admin)
- [Django <=> Python](https://docs.djangoproject.com/en/dev/faq/install/#what-python-version-can-i-use-with-django)
- [Django value sensitive unique together](https://stackoverflow.com/questions/16474552/is-there-any-more-elegant-way-to-add-a-value-sensitive-unique-together-constrain#answer-59939626)
- [DRF serialzer write only fields](https://stackoverflow.com/questions/34989915/write-only-read-only-fields-in-django-rest-framework#answer-36771366)
- [Locale error: unsupported locale setting](https://stackoverflow.com/questions/14547631/python-locale-error-unsupported-locale-setting#answer-14548156)
- [Locale problem in Docker](https://serverfault.com/questions/54591/how-to-install-change-locale-on-debian#answer-894545)
- [Celery timezone types](https://stackoverflow.com/questions/13866926/is-there-a-list-of-pytz-timezones)
- [Python date types](https://www.w3schools.com/python/python_datetime.asp)
- [Convert Python file to .exe](https://m.youtube.com/watch?feature=youtu.be&v=UZX5kH72Yx4)
- [Time complexity (big O)](https://wiki.python.org/moin/TimeComplexity)
- [Number of Gunicorn workers in Kubernetes](https://forum.djangoproject.com/t/gunicorn-workers-in-kubernetes/7918/2)
- [3rd-party Python profiler](https://github.com/plasma-umass/scalene)
- [Clean code python book](https://github.com/SepehrRasouli/clean-code-python)
- [FastAPI & Poetry standard Dockerfile](https://github.com/orgs/python-poetry/discussions/1879#discussioncomment-216865)
- [Bypass Cloudflare protection](https://github.com/FlareSolverr/FlareSolverr)

## File

- Open modes:

  ![](python/file_open_modes.png)

- Open modes decision tree:

  ![](python/file_open_modes_decision_tree.png)

## Class & Function

- Get full path:

  ```python
  import os
  import inspect

  def foo():
    pass

  print(os.path.abspath(inspect.getfile(foo)))

  class Bar:
    pass

  print(os.path.abspath(inspect.getfile(Bar.__class__)))
  ```

## Modules & Packages

- Get all import able modules & packages:

  ```python
  import pkgutil
  search_path = ['.'] # set to None to see all modules importable from sys.path
  all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
  print(all_modules)
  ```

## Celery

- Kill celery process:

  ```shell
  kill -9 $(ps aux | grep celery | grep -v grep | awk '{print $2}' | tr '\n' ' ') > /dev/null 2>&1
  ```

- View worker logs:

  ```shell
  celery -A <worker name: karestoon> worker --loglevel=info
  ```

## PIP

- Install from source (Unix path):

  ```shell
  pip install file:///path/to/package
  ```

## Operators

- Overview

  ![](python/operators.jpg)

- The "i" symbol means "in place"
- The "a" symbol means "asynchronous"
- The "r" symbol means "reverse"
- When we are implementing the "Rich comparison" method we should return a new object, in the other hand for the "Augmented assignment arithmetic" method we should update the current object

## Other

- cProfile example:

  ![](python/cprofile_example.jpg)
