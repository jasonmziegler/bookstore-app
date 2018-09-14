# app/catalog/__init__.py
from flask import Blueprint

main = Blueprint('main', __name__, template_folder='templates')







#import at bottom to avoid cross referencing errors because routes
#imports main
from app.catalog import routes
