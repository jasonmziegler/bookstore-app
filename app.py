from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for

from flask_sqlalchemy import SQLAlchemy

DEBUG = True

app = Flask(__name__)

app.config.update(

    SECRET_KEY = 'topsecret',
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Ushlyper@localhost/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

db = SQLAlchemy(app)


@app.route('/index')
@app.route('/')
def index():
    return 'Hello World!'

@app.route('/new/')
def query_string(greeting='hola!'):
    greeting = request.args.get('greeting', greeting)
    return '<h1>{}</h1>'.format(greeting)

@app.route('/user')
@app.route('/user/<name>')
def no_query_string(name='Jason'):
    return '<h1>{}</h1>'.format(name)

@app.route('/temp')
def temp():
    return render_template('hello.html')

# JINJA TEMPLATES
@app.route('/watch')
def movies():
    movie_list = ['Blackhawk Down', 'Aliens',
                'The Predator',
                'John Wick',
                'The Matrix']
    return render_template('movies.html', movies=movie_list, name='Harry')

@app.route('/tables')
def  movies_plus():
    movies_dict = {'Blackhawk Down': 298.9,
                'Aliens': 2.39,
                'The Predator': 0.092,
                'John Wick': 29.3,
                'The Matrix': 9000}
    return render_template('table_data.html', movies=movies_dict, name='Harry')

@app.route('/filters')
def filter_data():
    movies_dict = {'Blackhawk Down': 298.9,
                'Aliens': 2.39,
                'The Predator': 0.092,
                'John Wick': 29.3,
                'The Matrix': 9000}
    return render_template('filter_data.html',
                          movies=movies_dict,
                          name=None,
                          film='a christmas carol')

@app.route('/macros')
def jinja_macros():
    movies_dict = {'Blackhawk Down': 298.9,
                'Aliens': 2.39,
                'The Predator': 0.092,
                'John Wick': 29.3,
                'The Matrix': 9000}
    return render_template('using_macros.html', movies=movies_dict)

class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=False)

    def __init__(self, name):
        #self.id = id
        self.name= name

    def __repr__(self):
        return '{}'.format(self.name)

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    #Relationship
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, author, avg_rating, book_format, image, num_pages,
                pub_id):

        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)

if __name__ == '__main__':
    #app.static_folder = 'static'
    db.create_all()
    app.run(debug=DEBUG)
