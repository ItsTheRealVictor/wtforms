from flask import Flask, request, render_template, redirect, url_for, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddSnackForm
app = Flask(__name__)

app.config['SECRET_KEY'] = "farts"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False 
app.debug = True
debug = DebugToolbarExtension(app)



@app.route('/snacks/new', methods=['GET', 'POST'])
def add_snack():
	form = AddSnackForm()
	print(form.name.data)
	print(form.price.data)
	print(form.quantity.data)
	if form.validate_on_submit():
		return redirect('/')
	else:
		return render_template('home.html', form=form)





