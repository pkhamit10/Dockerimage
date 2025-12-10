# Simple Flask + MySQL Web App

Simple example web application using Python Flask and a MySQL database. Includes instructions for local development and Docker.

## Requirements
- Install required dependencies
- Install and Configure Database
- Start Database Service
- Install and configure Web Server
- Start Web Server

## Repository layout (example)
- app.py              # Flask application entry
- Dockerfile
- README.md

## Install Required Dependencies
Python and its dependencies

### Install Required Dependencies

On Debian/Ubuntu, update package lists and install Python 3:

```sh
sudo apt-get update
sudo apt-get install -y python3
```

Verify the installation:

```sh
python3 --version
```
## Map the standard input using '-i' parameter and terminal using 't'
## Append a bash command to run the bash command when it starts the container and work on that particular container
```sh
docker run -it ubuntu bash
```

## Install pip
```sh
apt install -y python3 python3-pip
```

## Install Flask
```sh
pip3 install flask
```

 ## Install My-sql
```sh
pip install pymysql flask-mysqldb
```

## Start Web Server
FLASK_APP=app.py flask run --host=0.0.0.0

## Test
Open a browser and go to URL
```sh
http://<IP>:5000                            => Welcome
http://<IP>:5000/how%20are%20you            => I am good, how about you?
http://<IP>:5000/read%20from%20database     => Joe
```