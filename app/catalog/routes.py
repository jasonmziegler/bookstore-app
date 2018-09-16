from app.catalog import main
from app import db
from app.catalog.models import  Book, Publication
from flask import render_template, flash, request, redirect, url_for
from flask_login import login_required

@main.route('/')
def hello():
    books = Book.query.all()
    return render_template('home.html', books=books)

@main.route('/display/publisher/<publisher_id>')
def display_publisher(publisher_id):
    publisher = Publication.query.filter_by(id=publisher_id).first()

    publisher_books = Book.query.filter_by(pub_id = publisher.id).all()

    return render_template('publisher.html', publisher=publisher, publisher_books=publisher_books)


@main.route('/book/delete/<book_id>', methods=['GET','POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get(book_id)
    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        flash('Book deleted successfully')
        return redirect(url_for('main.hello'))
    return render_template('delete_book.html', book=book, book_id=book.id)
