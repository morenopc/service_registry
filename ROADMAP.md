# Service Registry

## Approach
Get a registry web service API up and running with a stronge base, easy to expand and scale, as simple as possible that will pass all behave tests.

## Resources
- Python 3.6.4 / Django 2.0.3
- Django REST framework 3.7.7 (and other apps)

## Road map
1. Setup development environment
2. install and config (python, django and so on) and start project
3. install and config Django REST framework (and other apps)
4. write some code, pass the tests and commit (while push: if all_tests_passed: push = True)
5. create a pull request


## Setup development 

### Install python 3.6.4 with pyenv

Follow the  Installation / Update / Uninstallation at [https://github.com/yyuu/pyenv-installer#installation--update--uninstallation](https://github.com/yyuu/pyenv-installer#installation--update--uninstallation)

```
$ pyenv update
```
Install python 3.6.4
```
$ pyenv install 3.6.4
$ pyenv global 3.6.4
$ pyenv versions
  system
* 3.6.4 (set by /home/moreno/.pyenv/version)
$ python -V
Python 3.6.4
```
