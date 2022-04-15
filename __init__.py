from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

#app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
#app.config['SECRET_KEY'] = getenv('SECRET_KEY')
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app = Flask(__name__)
app = Flask(__name__, template_folder='templates')
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
db.init_app(app)


db = SQLAlchemy(app)

from application import routes
