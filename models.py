import uuid
from . import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Book(db.Model):
  id = db.Column(db.CHAR(50), primary_key=True)
  title = db.Column(db.String)
  author = db.Column(db.String)
  is_checked_out = db.Column(db.Boolean)

  def __init__(self, id, title, author, is_checked_out):
      self.id = id
      self.title = title
      self.author = author
      self.is_checked_out = is_checked_out

books = [
    Book(id=uuid.uuid4(), title="Harry Potter and the Sorcerer's Stone", author='J.K. Rowling', is_checked_out=True),
    Book(id=uuid.uuid4(), title='Harry Potter and the Chamber of Secrets', author='J.K. Rowling', is_checked_out=True),
    Book(id=uuid.uuid4(), title='Harry Potter and the Prisoner of Azkaban', author='J.K. Rowling', is_checked_out=True)
    ]
db.drop_all()
db.create_all()
db.session.bulk_save_objects(books)
db.session.commit()
