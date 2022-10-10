from flask import Flask

app = Flask(__name__)
app.secret_key = 'hello_world'
app.config.from_object(__name__)

from . views import *