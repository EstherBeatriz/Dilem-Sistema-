from flask_mysqldb import MySQL


mysql = MySQL()

# Configurações da aplicação
DEBUG = True

# Configurações do banco de dados
DATABASE = {
    'host': 'localhost',
    'user': 'root_dev',
    'password': 'admin',
    'db': 'bd_dilem'
}

# Configurar a aplicação para usar o MySQL
def init_app(app):
    app.config['MYSQL_HOST'] = DATABASE['host']
    app.config['MYSQL_USER'] = DATABASE['user']
    app.config['MYSQL_PASSWORD'] = DATABASE['password']
    app.config['MYSQL_DB'] = DATABASE['db']
    mysql.init_app(app)


from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root_dev'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'bd_dilem'
 
mysql = MySQL(app)

