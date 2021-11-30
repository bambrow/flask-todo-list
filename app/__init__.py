from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ineedtosetthisthisisatupsecretbutidontcareijustwantmyapptowork'
app.config['MONGODB_DB'] = 'flask-todo-list'
app.config['MONGODB_HOST'] = 'ds149934.mlab.com'
app.config['MONGODB_PORT'] = 49934
app.config['MONGODB_USERNAME'] = 'admin'
app.config['MONGODB_PASSWORD'] = 'admin'

db = MongoEngine(app)

from app import views, models
