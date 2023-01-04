# web_server_pi
Setting up a web server for my raspberry pi. Just another hobby

Configuring my RPI 4 so that I can easily access / monitor the RPI 4 from my desktop.

#### Roadmap
Set up database (sql) on RPI4 -> Set up website (next.js) -> SEO optimization  

### Set up raspberry pi for remote access 
1. Setting up RDP (Remote Desktop protocol) on the pi (https://www.youtube.com/watch?v=55sUIufYofE)

2. DHCP reservation for PI. Go to gateway (192.168.10.1) and configure DHCP reservation for your pi (might need mac address)

3. Setting up Static IP on my RPI 4 (https://www.makeuseof.com/raspberry-pi-set-static-ip/) 

4. Enable SSH access

### Set up Docker + Jenkins on RPI4

Docker tutorial https://www.youtube.com/watch?v=9zUHg7xjIqQ

## Additional info
1. VIM commands https://coderwall.com/p/adv71w/basic-vim-commands-for-getting-started

## Docker reference
docker-compose -f docker-compose.yml up -d
### Commands for postgres (docker-compose)
winpty docker exec -it web_server_pi_db_1 psql -U postgres

### inside psql
create database test;
\c <database_name>
\l #shows database

## Django

python manage.py runserver

### Set up
Anytime you update the model, we need to migrate
python manage.py makemigrations
python manage.py migrate
python manage.py startapp <name>
python manage.py shell # quick way of adding stuff using shell
You need to change the settings file inside your project so that django knows where to look for changes in the model

### Seeding fake data into your database
Use faker library to fake data
python .\manage.py seed-data

### Explaining Models
Django models are lazy, you can write the query but it won't execute until you need it

Each query starts with a Manager ->
Model.objects # this will return a Manager object 
Model.objects.all() returns a QuerySet<>




## Virtual Environment
### create environment first 
python -m venv env # this creates your virtual env inside the env folder
pip install -r requirements.txt --no-index --find-links file:///tmp/packages

## Deployment
Figure this shit out on fri / weekend
Dockerizing your python webserver 
What is WSGI - https://www.youtube.com/watch?v=_rLEzgNiuJk
SETTING UP WSGI SERVER - https://www.youtube.com/watch?v=YnrgBeIRtvo


### Extra stuff
maybe create another bot for feed - see if you can stream it from twitter api straight

## How to run
### DB
cd web_server_pi -> docker-compose docker-compose.yml -d up 
### webserver
Run virtual env -> python manage.py runserver