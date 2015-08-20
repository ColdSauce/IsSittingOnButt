from flask import Flask
app = Flask(__name__)


isPressed = False
def getPressedHtml():
	return "Pressed"

def getNotPressedHtml():
	return "Not Pressed"

@app.route("/released")
def released():
	global isPressed
	isPressed = False

@app.route("/pressed")
def pressed():
	global isPressed
	isPressed = True
	
@app.route("/")
def index():
	global isPressed
	#if isPressed:
	#	return getPressedHtml()	
	#else:
	#	return getNotPressedHtml()
        return render_template("templates/index.html")

if __name__ == "__main__":
    app.run()
