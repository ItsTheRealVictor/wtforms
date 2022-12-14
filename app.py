from flask import Flask, request, render_template, redirect, url_for, flash
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "farts"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False 
debug = DebugToolbarExtension(app)

@app.route('/')
def main_page():
  return render_template('home.html')

