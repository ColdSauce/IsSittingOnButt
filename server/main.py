from flask import Flask, render_template
from twitter import *

app = Flask(__name__)


t = Twitter(
    auth=OAuth('3329033923-exeAQZYaPtyqjnuWqnpyTbKlVysLzmtJ23FnQhY', '8EpD3yvv4HaSOs7iS5bsx42Y7EUzYQ1lLxG4NTr11bbtc', 'kPf0HlyvBfqDcBZOocCgz4AJo', 'uA1hc2kne09Tvv2eloSKZbyCiYgc2j99aHOorazfWot3iiuRvZ'))

isPressed = False

def getPressedHtml():
    return render_template("isPressed.html")

def getNotPressedHtml():
    return render_template("isNotPressed.html")

@app.route("/released")
def released():
	global isPressed
	isPressed = False
        return getNotPressedHtml()

@app.route("/pressed")
def pressed():
	global isPressed
	isPressed = True
        return getPressedHtml()

def last_tweet_yes():
  last_tweet = t.statuses.user_timeline(screen_name="stestefanfan")[0]['text']
  if last_tweet == "yes":
    return True
  else:
    return False

@app.route("/")
def index():
	global isPressed
  # Insert twitter account here
	if last_tweet_yes() == True:
		return getPressedHtml()
        else:
		return getNotPressedHtml()



if __name__ == "__main__":
    app.run(debug = True)
