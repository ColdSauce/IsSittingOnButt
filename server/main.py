from flask import Flask, render_template

app = Flask(__name__)


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
	
@app.route("/")
def index():
	global isPressed
	if isPressed:
		return getPressedHtml()	
        else:
		return getNotPressedHtml()

if __name__ == "__main__":
    app.run(debug = True)
