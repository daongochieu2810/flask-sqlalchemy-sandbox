from flask import Flask
import os
prod = 'postgres://efhcrdoezlcoqj:e5fab140e8f6aa9fff97786f021003219d0f10f6abdef01f9ce6a6024595d0e5@ec2-44-207-126-176.compute-1.amazonaws.com:5432/d90qs881urf4m9'
app = Flask(__name__)
app.secret_key = 'hello_world'
app.config.from_object(__name__)
database_path = prod #'postgresql://hieu:hieu@localhost:5432/bt5110'
app.config['SQLALCHEMY_DATABASE_URI'] = database_path

from . views import *