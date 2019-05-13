
from jinja2 import StrictUndefined
import requests
import json
from flask import Flask, render_template, request, flash, redirect, session, url_for
from flask_debugtoolbar import DebugToolbarExtension



app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "kjhdsf8234"

app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
	"""Homepage."""
	return render_template("base.html")

@app.route("/gifs")
def find_gifs():
	search = request.args.get('search')

	response = requests.get("http://api.giphy.com/v1/gifs/search?q="+search+"&api_key= DLCVuTK6KZExOS7JoMq82bi5MaI6EbWO&limit=10")
	data = response.json()
	if response.ok:
		gifs = data['embed_url']
	else:
		flash("No gifs found")
		gifs = []

	return render_template("gif.html",data=data,gifs=gifs)

if __name__ == "__main__":
	app.debug = True


	DebugToolbarExtension(app)

	app.run()
