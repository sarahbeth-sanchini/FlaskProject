#app is the parent package
#catelog is the sub package
#this file is catalog's __init__.py file

from flask import Blueprint

#create an instance to use the class "Blueprint"
#Remember that __name__ is a special python variable that sets the scope
main = Blueprint('main', __name__, template_folder='templates')

#put at the bottom so no circular logic/dependancy issues with cross-importing blueprints
from app.catalog import routes