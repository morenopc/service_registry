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

## Rest Framework JWT (JSON web token)

### Get Token

```
> POST /api-token-auth/ HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.52.1
> Accept: */*
>
< HTTP/1.1 200 OK
< Content-Type: application/json
< Content-Length: 221

$ curl -H "Content-Type:application/json" -d '{"username":"admin","password":"p@SS4w0rD4"}' http://localhost:8000/api-token-auth/

{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTIxMTUyNTM5LCJlbWFpbCI6ImFkbWluQG1haWwuY29tIiwib3JpZ19pYXQiOjE1MjA4OTMzMzl9.4ewU0nAA1q72me_Su7plzylVjMnwNEbkcwx_uxY7anM"}
```

### Verify Token

```
> POST /api-token-verify/ HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.52.1
> Accept: */*
>
< HTTP/1.1 200 OK
< Content-Type: application/json
< Content-Length: 221

$ curl -H "Content-Type:application/json" -d '{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTIxMTUyNTM5LCJlbWFpbCI6ImFkbWluQG1haWwuY29tIiwib3JpZ19pYXQiOjE1MjA4OTMzMzl9.4ewU0nAA1q72me_Su7plzylVjMnwNEbkcwx_uxY7anM"}' http://localhost:8000/api-token-verify/

{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTIxMTUyNTM5LCJlbWFpbCI6ImFkbWluQG1haWwuY29tIiwib3JpZ19pYXQiOjE1MjA4OTMzMzl9.4ewU0nAA1q72me_Su7plzylVjMnwNEbkcwx_uxY7anM"}
```

### Refresh Token

```
> POST /api-token-refresh/ HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.52.1
> Accept: */*
>
< HTTP/1.1 200 OK
< Content-Type: application/json
< Content-Length: 221

$ curl -v -H "Content-Type:application/json" -d '{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTIxMTUyNTM5LCJlbWFpbCI6ImFkbWluQG1haWwuY29tIiwib3JpZ19pYXQiOjE1MjA4OTMzMzl9.4ewU0nAA1q72me_Su7plzylVjMnwNEbkcwx_uxY7anM"}' http://localhost:8000/api-token-refresh/

{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTIxMTUzMjQ0LCJlbWFpbCI6ImFkbWluQG1haWwuY29tIiwib3JpZ19pYXQiOjE1MjA4OTMzMzl9.VQD9bqa8WR1Y2-7ecghZ2y-7T9tOstMhU7incJXlhc0"}
```

## Rest Framework

### Add service

```
> POST /api/v1/registries/ HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.52.1
> Accept: */*
>
< HTTP/1.1 201 Created
< Content-Type: application/json
< Content-Length: 63

curl -v -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTIxMTUzMjQ0LCJlbWFpbCI6ImFkbWluQG1haWwuY29tIiwib3JpZ19pYXQiOjE1MjA4OTMzMzl9.VQD9bqa8WR1Y2-7ecghZ2y-7T9tOstMhU7incJXlhc0" \
-H "Content-Type:application/json" \
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
< Content-Type: application/json
< Content-Length: 31

curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTIxMTUzMjQ0LCJlbWFpbCI6ImFkbWluQG1haWwuY29tIiwib3JpZ19pYXQiOjE1MjA4OTMzMzl9.VQD9bqa8WR1Y2-7ecghZ2y-7T9tOstMhU7incJXlhc0" \
-H "Content-Type:application/json" \
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
< Content-Type: application/json
< Content-Length: 29

curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTIxMTUzMjQ0LCJlbWFpbCI6ImFkbWluQG1haWwuY29tIiwib3JpZ19pYXQiOjE1MjA4OTMzMzl9.VQD9bqa8WR1Y2-7ecghZ2y-7T9tOstMhU7incJXlhc0" \
-H "Content-Type:application/json" "http://localhost:8000/api/v1/search/?service=test1"

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
< Content-Type:application/json
< Content-Length: 28

curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTIxMTUzMjQ0LCJlbWFpbCI6ImFkbWluQG1haWwuY29tIiwib3JpZ19pYXQiOjE1MjA4OTMzMzl9.VQD9bqa8WR1Y2-7ecghZ2y-7T9tOstMhU7incJXlhc0" \
-H "Content-Type:application/json" \
"http://localhost:8000/api/v1/search/?service=test"

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
< Content-Type:application/json
< Content-Length: 70

curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTIxMTUzMjQ0LCJlbWFpbCI6ImFkbWluQG1haWwuY29tIiwib3JpZ19pYXQiOjE1MjA4OTMzMzl9.VQD9bqa8WR1Y2-7ecghZ2y-7T9tOstMhU7incJXlhc0" \
-H "Content-Type:application/json" \
"http://localhost:8000/api/v1/search/"

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
< Content-Type:application/json
< Content-Length: 58

curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTIxMTUzMjQ0LCJlbWFpbCI6ImFkbWluQG1haWwuY29tIiwib3JpZ19pYXQiOjE1MjA4OTMzMzl9.VQD9bqa8WR1Y2-7ecghZ2y-7T9tOstMhU7incJXlhc0" \
-H "Content-Type:application/json" \
"http://localhost:8000/api/v1/search/?version=0.0.1"

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
< Content-Type: application/json
< Content-Length: 20

curl -X PUT -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTIxMTUzMjQ0LCJlbWFpbCI6ImFkbWluQG1haWwuY29tIiwib3JpZ19pYXQiOjE1MjA4OTMzMzl9.VQD9bqa8WR1Y2-7ecghZ2y-7T9tOstMhU7incJXlhc0" \
-H "Content-Type:application/json" \
-d '{
  "service":"ttestt",
  "version":"0.1.3"
 }' \
 http://localhost:8000/api/v1/update/1/

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
< Content-Type: application/json
< Content-Length: 38

curl -X DELETE \
-H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTIxMTUzMjQ0LCJlbWFpbCI6ImFkbWluQG1haWwuY29tIiwib3JpZ19pYXQiOjE1MjA4OTMzMzl9.VQD9bqa8WR1Y2-7ecghZ2y-7T9tOstMhU7incJXlhc0" \
http://localhost:8000/api/v1/delete/4/

{"service":"test3","change":"removed"}
```

## Unit Tests

### Run (test services)
```
registry$ python manage.py test services
```
