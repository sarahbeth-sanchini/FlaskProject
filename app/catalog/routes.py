from app.catalog import main
from app import db
from app.catalog.models import Book, Publication
from flask import render_template

#we dont have access to the flask instance on a global level
#therefore we use the Blueprint instead
@main.route('/')
def display_books():
    books = Book.query.all()
    return render_template('home.html', books=books)
    #need to pass the books instance to be rendered

@main.route('/display/publisher/<publisher_id>')
#within the angular brackets is the parameter being sent during runtime
def display_publisher(publisher_id):
    publisher = Publication.query.filter_by(id=publisher_id).first()
    publisher_books = Book.query.filter_by(pub_id = publisher.id).all()

    return render_template('publisher.html', publisher=publisher, publisher_books=publisher_books)
