import uuid
from . import app
from .app import admin
from .models import db, Book
from flask import flash, redirect, render_template, request, url_for

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_new_book():
    if request.method == 'POST':
        id = uuid.uuid4()
        title = request.form['title']
        author = request.form['author']
        is_checked_out = True
        book_data = Book(id, title, author, is_checked_out)

        db.session.add(book_data)
        db.session.commit()
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        rowid = request.form['rowid']
        check_in = Book.query.filter_by(id=rowid).update(dict(is_checked_out=False))
        db.session.commit()
        flash('Book was checked in!', 'success')
        return redirect(url_for('book.index_view'))
