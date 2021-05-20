# flask-temperature-api
API converting temperatures built with Flask

## Technical stacks
Python3.9, Flask2.0, Python Unittest, Heroku
- By using Flask, can write an API endpoint with minimum configuration and coding. It's light-weight microservice framework, and widely used for projects providing RESTful API backend.
- Python's Unittest package provides good unit testing functionality, so I've built test cases based on it.
- This api is deployed on Heroku instance, and API endpoint is https://flask-temperature-api.herokuapp.com/api/v1/converter
- For the API endpoint structure, I followed common practices to build API by proceeding `api` URL and following `v1` to recognize API endpoint with normal URLs and provide specific version info
- Testing api is done via `Postman` and `CURL`, and sample `CURL` command is below
```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"type":"f","value":"35"}' \
  https://flask-temperature-api.herokuapp.com/api/v1/converter

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"type":"c","value":"0"}' \
  https://flask-temperature-api.herokuapp.com/api/v1/converter
```

## Configuring and Running API on Local
Assuming Python3.9 is installed in local environment

##### Create virtualenv

```bash
virtualenv venv
```

##### Activate virtualenv

- For Linux/Mac Platform
```bash
source venv/bin/activate
```

- For Windows platform
```bash
source venv/script/activate
```


##### Install python packages

```bash
pip install -r requirements.txt
```

##### Running dev server
```bash
python main.py
```

##### Testing API
```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"type":"f","value":"35"}' \
  https://localhost:5000/api/v1/converter
```

##### Run unittest
```bash
python -m unittest tests/test_api.py
```

## Deployment to Heroku
- Please check heroku's deployment guide for Python. 
https://devcenter.heroku.com/articles/git
https://devcenter.heroku.com/articles/python-gunicorn
- Why did I deploy it to heroku? Because it's free to deploy, and easy to deploy it by using git command, and no DevOps required. It's perfect to test this kind of API.
