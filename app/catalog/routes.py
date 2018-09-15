from app.catalog import main
from app import db
from app.catalog.models import  Book, Publication
from flask import render_template

@main.route('/')
def hello():
    books = Book.query.all()
    return render_template('home.html', books=books)
