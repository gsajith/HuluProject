
from flask import *
import urllib2
import json 
import requests
import random 
import time
import re
import operator

main = Blueprint('main', __name__, template_folder='views')
dictionary = open("dict.txt", "r")
results = [] 
guesses = []
guess =""
restart = True
data = []
@main.route('/')
def main_route():
	global restart
	global data
	global results
	global guess
	global guesses
	if restart:
		print "restart"
		url = "http://gallows.hulu.com/play?code=gsajith@umich.edu"
		d = urllib2.urlopen(url)
		data = json.load(d)
		results=[]
		guesses=[]
		options={
			'status':data['status'],
			'token':data['token'],
			'remaining_guesses':data['remaining_guesses'],
			'state':data['state'],
			'results':results
		}
		restart = False
		return render_template("index.html", **options) 
	else:
		print "no restart"
		token = data['token']
		guess = formulate_guess(data['state']) 
		url = "http://gallows.hulu.com/play?code=gsajith@umich.edu&token="+token+"&guess="+guess
		d = urllib2.urlopen(url)
		data = json.load(d)
		results.append("Guessing '" + guess + "'")
		options={
                        'status':data['status'],
                        'token':data['token'],
                        'remaining_guesses':data['remaining_guesses'],
                        'state':data['state'],
                        'results':results
                }
		guesses.append(guess.lower())
		if data['status'] != 'ALIVE':
			restart = True
		return render_template("index.html", **options)

def formulate_guess(state):
	global guesses
	words = state.split()
	resultArray={}
	for word in words:
		temp = word
		print temp
		if word.find("_") != -1:
			word = word.replace("_", "[a-z]")
			word+="$"
			word = "^" + word
			for line in dictionary:	
				if len(line) == len(temp)+1:
					result = re.search(word, line, re.IGNORECASE)
					if result is not None: 
						i = 0
						for c in temp:
							if temp[i] == '_':
								foundChar = result.group(0)[i].lower()
								if foundChar in resultArray: resultArray[foundChar] = resultArray[foundChar]+1
								else: resultArray[foundChar] = 1
							i = i+1
			dictionary.seek(0)
	print resultArray
	maxChar = str(max(resultArray, key=resultArray.get))
	while maxChar.lower() in guesses:
		del resultArray[maxChar]
		maxChar = str(max(resultArray, key=resultArray.get))
	guess = maxChar
	return guess		
