# IMPLEMENTATION INFO
I chose to implement this hangman solver as a web app, mostly for fun and 
partially so I could show my solver to some friends of mine.  It's implemented
using Python and Flask.

My app switches between two high-level states:  Restart and no-restart.  
In the restart state, either the user has just connected (so a new hangman 
puzzle needs to be loaded) or the previous puzzle was completed, so a new
puzzle needs to be loaded.  In this state, the correct URL is fetched 
to get a new puzzle with a new token.
In the no-restart state, a puzzle is currently in progress so no new 
puzzle is fetched.  In this state, the token is maintained so that
the puzzle session can continue.

# GUESS - GENERATION
Within the no-restart state, the app starts formulating guesses based on
conditional probability.  
e.g. When the entirety of the phrase to guess
is blank, it will go through the loaded dictionary file and find
the most common character to guess.

When the phrase starts to fill up with correct letters, it will search
the dictionary only for words which would match the regex specified 
by the combination of blanks and letters.
e.g. the incomplete word EXA-I-ED would be converted to the 
regex ^EXA[a-zA-Z]I[a-zA-Z]ED$ and then searched for, and the conditional
probability of the next best character to guess would be based on these results.

I also keep track of a list of already guessed letters, just so it doesn't 
keep guessing a previously-most-common-character which is still-most-common.

# SETUP INFO
Run `virtualenv venv --distribute` 

Run `source venv/bin/activate`  Sets up and activates the virtual environment

Run `pip install -r requirements.txt`  Installs required files

Run the app:  `gunicorn -b <URL:PORT HERE> app:app -t 0`

Replace <URL:PORT HERE> with the IP/URL of your server machine, or just localhost.

Visit the site specified by your URL.  The site will auto-refresh every second with
a new guess.
