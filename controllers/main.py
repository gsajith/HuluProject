
from flask import *

main = Blueprint('main', __name__, template_folder='views')

@main.route('/')
def main_route():
    return render_template("index.html")