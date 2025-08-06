# Flask Layered Template

a Flask template with 3-tier layered architecture design  
a simple signup api code is included for eaiser understanding of the architecture  

3-tier  
1. model layer : layer with singleton DAO  
2. service layer : layer where business logic is taken care of  
3. view layer : layer where endpoints/access/return are described  

the template uses mariadb/mysql by default

## project structure

root  
ㄴ app.py  
ㄴ config/  
&nbsp;&nbsp;&nbsp;&nbsp;ㄴ__init__.py  
&nbsp;&nbsp;&nbsp;&nbsp;ㄴproduction.py  
&nbsp;&nbsp;&nbsp;&nbsp;ㄴdevelopment.py  
&nbsp;&nbsp;&nbsp;&nbsp;ㄴtest.py  
ㄴ model/  
&nbsp;&nbsp;&nbsp;&nbsp;ㄴ__init__.py  
&nbsp;&nbsp;&nbsp;&nbsp;ㄴauth_dao.py  
ㄴ service/  
&nbsp;&nbsp;&nbsp;&nbsp;ㄴ__init__.py  
&nbsp;&nbsp;&nbsp;&nbsp;ㄴauth_service.py  
ㄴ view/  
&nbsp;&nbsp;&nbsp;&nbsp;ㄴ__init__.py  
&nbsp;&nbsp;&nbsp;&nbsp;ㄴauth_view.py  

## development environment setting

- create virtual env and install requriements

```bash
$ python3 -m venv virtualenv
$ pip install -r requriements.txt
```

- set env variables  

create .env file at project root

```
FLASK_APP=app.py
FLASK_ENV=development
APP_CONFIG_FILE=/path/to/development.py
```

- set configuration  

modify /config/development.py for your project

- run server

```bash
flask run
```
