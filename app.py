from . import app
from .models import Book, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

class BookView(ModelView):
    column_list = ['title', 'author']

admin = Admin(app, template_mode='bootstrap3')
admin.add_view(BookView(Book, db.session))

from . import routes
