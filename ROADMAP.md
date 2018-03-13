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
5. PEP8
6. create a pull request
7. add JSON Web Tokens (JWT) REST framework authentication
8. write and pass unit tests
9. write and pass behave tests


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

### Run local server

```
$ python -m venv env
$ . env/bin/activate
(env) $ pip install -r requirements.txt
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
(env) $ python manage.py runserver
```

## Rest Framework

### Add service

```
> POST /api/v1/registries/ HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.52.1
> Accept: */*
> Content-Type:application/json
> Content-Length: 44
>
< HTTP/1.1 201 Created
< Content-Type: application/json

curl -H "Content-Type:application/json" \
-d '{
  "service":"test",
  "version":"0.0.1"
 }' \
 http://localhost:8000/api/v1/registries/

{"service":"test","version":"0.0.1","change":"created"}
```

### Find service

```
> GET /api/v1/search/?service=test3 HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.52.1
> Accept: */*
>
< HTTP/1.1 200 OK
< Date: Fri, 09 Mar 2018 15:38:14 GMT
< Server: WSGIServer/0.2 CPython/3.6.4
< Content-Type: application/json
< Content-Length: 31

curl -v "Content-Type: application/json" \
"http://localhost:8000/api/v1/search/?service=test3&version=0.0.1"

{"service":"test3","version":"0.0.1","count":3}
```

### Finding non existing service

```
> GET /api/v1/search/?service=test1 HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.52.1
> Accept: */*
>
< HTTP/1.1 404 Not Found
< Date: Fri, 09 Mar 2018 18:49:09 GMT
< Server: WSGIServer/0.2 CPython/3.6.4
< Content-Type: application/json
< Content-Length: 29

curl -v "Content-Type: application/json" "http://localhost:8000/api/v1/search/?service=test1"

{"service":"test1","count":0}
```

### Finding service without version

```
> GET /api/v1/search/?service=test HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.52.1
> Accept: */*
>
< HTTP/1.1 200 OK
< Date: Fri, 09 Mar 2018 18:45:22 GMT
< Server: WSGIServer/0.2 CPython/3.6.4
< Content-Type: application/json
< Content-Length: 28

curl -v "Content-Type: application/json" "http://localhost:8000/api/v1/search/?service=test"

{"service":"test","count":3}
```

### Exceptions

#### Search without parameter
```
> GET /api/v1/search/ HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.52.1
> Accept: */*
>
< HTTP/1.1 500 Internal Server Error
< Date: Fri, 09 Mar 2018 18:50:41 GMT
< Server: WSGIServer/0.2 CPython/3.6.4
< Content-Type: application/json
< Content-Length: 70

curl "Content-Type: application/json" "http://localhost:8000/api/v1/search/"

{"detail":"Search parameters (service or version) could not be found"}
```

#### Search without service
```
> GET /api/v1/search/?version=0.0.1 HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.52.1
> Accept: */*
>
< HTTP/1.1 500 Internal Server Error
< Date: Fri, 09 Mar 2018 18:50:53 GMT
< Server: WSGIServer/0.2 CPython/3.6.4
< Content-Type: application/json
< Content-Length: 58

curl "Content-Type: application/json" "http://localhost:8000/api/v1/search/?version=0.0.1"

{"detail":"Search parameter (service) could not be found"}
```

### Updating a service
```
> PUT /api/v1/update/1/ HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.52.1
> Accept: */*
> Content-Type:application/json
> Content-Length: 46
>
< HTTP/1.1 200 OK
< Date: Fri, 09 Mar 2018 20:05:52 GMT
< Server: WSGIServer/0.2 CPython/3.6.4
< Content-Type: application/json
< Content-Length: 20

curl -X PUT -H "Content-Type:application/json" -d '{
  "service":"ttestt",
  "version":"0.1.3"
 }'  http://localhost:8000/api/v1/update/1/

{"change":"changed"}
```

### Removing a service
```
> DELETE /api/v1/delete/4/ HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.52.1
> Accept: */*
>
< HTTP/1.1 200 OK
< Date: Fri, 09 Mar 2018 20:37:25 GMT
< Server: WSGIServer/0.2 CPython/3.6.4
< Content-Type: application/json
< Content-Length: 38

curl -X DELETE http://localhost:8000/api/v1/delete/4/

{"service":"test3","change":"removed"}
```
