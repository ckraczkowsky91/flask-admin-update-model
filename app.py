from . import app
from .models import Book, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

class BookView(ModelView):
    can_create = False
    can_delete = False
    can_edit = False
    column_list = ['title', 'author', 'is_checked_out']
    list_template = 'custom_list.html'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.static_folder = 'static'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.static_folder = 'static'

    def get_query(self):
        return self.session.query(self.model).filter(self.model.is_checked_out==True)

admin = Admin(app, name='Hogwarts Library', template_mode='bootstrap3', index_view=BookView(Book, db.session, name='Check In', url='/admin', endpoint='admin'))

from . import routes
