
from flask import *
import json
import urllib2

main = Blueprint('main', __name__, template_folder='views')

@main.route('/')
def main_route():
	return render_template("index.html")
@main.route('/getGeocode', methods = ['GET', 'POST'])
def geo_route():
	jsonGeocode = ''
	if request.method == "POST":
		address = request.json
		address = address.replace(' ', '+')
		url="https://maps.google.com/maps/api/geocode/json?address=%s&sensor=false" % address		
		response = urllib2.urlopen(url)
		jsonGeocode = response.read()
	return jsonGeocode

