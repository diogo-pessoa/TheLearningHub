Testing
---

Section to describe How to run tests on local development environment and describe testing running in [travis.com](https://app.travis-ci.com/)

- [Staging Environment](https://the-learning-hub-staging.herokuapp.com/)

### Automated Tests

For the automated testing this project leverages [travis.com](https://app.travis-ci.com/)

- [.travis.yml](/.travis.yml)
    - this file content describe steps executed during build

### Local tests

- make sure to apply migrations:

---
      $ python3 manage.py makemigrations
      $ python3 manage.py showmigrations 
      $ python3 manage.py migrate

- run tests

---
    # Run whole test suite
      $ python3 manage.py test 
    # Run test for a single app
      $ python3 manage.py test articles
    # For a single Class
      $ python3 manage.py test articles.test_views.TestArticlesViews

- Show Test coverage

---
    # make sure coverage is installed
      $ pip3 install coverage #is in app requirements should be installed already
    # Run run test to generate coverage report
      $ coverage run  --source=TheLearningHub manage.py test
    # get report 
      $ coverage report