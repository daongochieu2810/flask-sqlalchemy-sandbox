from flask import Flask
import os

app = Flask(__name__)
app.secret_key = 'hello_world'
app.config.from_object(__name__)
database_path = 'postgresql://hieu:hieu@localhost:5432/bt5110' #os.getenv('DATABASE_URL', 'postgresql://hieu:hieu@localhost:5432/bt5110')
app.config['SQLALCHEMY_DATABASE_URI'] = database_path

from . views import *