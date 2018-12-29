#########################################################################
# File Name: install_env.sh
# Author: ma6174
# Created Time: 2018年12月29日 星期六 14时53分53秒
#########################################################################
#!/bin/bash 
flask/bin/pip install flask
flask/bin/pip install flask-login
flask/bin/pip install flask-openid
flask/bin/pip install flask-mail
flask/bin/pip install flask-sqlalchemy
flask/bin/pip install sqlalchemy-migrate
flask/bin/pip install flask-whooshalchemy
flask/bin/pip install flask-wtf
flask/bin/pip install flask-babel
flask/bin/pip install guess_language
flask/bin/pip install guess_language-spirit
flask/bin/pip install flipflop
flask/bin/pip install coverage

flask/bin/pip install flask_migrate
flask/bin/pip install flask_bootstrap
flask/bin/pip install flask_moment
flask/bin/pip install elasticsearch
flask/bin/pip install dotenv
flask/bin/pip install jwt
flask/bin/pip install unicodeBlock
flask/bin/pip install requests
flask/bin/pip install flask-mysqldb 

flask/bin/pip install freeze
#flask/bin/pip uninstall flask-openid
#flask/bin/pip install git+git://github.com/mitsuhiko/flask-openid.git




#### database install  ###
mysql -u root -p

create database skin_db;
use skin_db;
create table user;

