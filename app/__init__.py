from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from app import classClass


UPLOAD_FOLDER = 'app\static\excel'

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


from app import routes

