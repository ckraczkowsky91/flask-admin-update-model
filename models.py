from . import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Book(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String)
  author = db.Column(db.String)

db.drop_all()
db.create_all()
