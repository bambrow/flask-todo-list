from app import db
import datetime
from flask_mongoengine.wtf import model_form


class Todo(db.Document):
    # create data model to map to Document object of database
    content = db.StringField(required=True, max_length=512)
    # content of to-do
    time = db.DateTimeField(default=datetime.datetime.now())
    # time of to-do
    status = db.IntField(default=0)
    # status of to-do

TodoForm = model_form(Todo)
# create TodoForm class
# this class is used for form validation
# in this way, the form validation is consistent with the database validation
