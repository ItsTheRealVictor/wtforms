from flask_wtf import FlaskForm
from wtforms import StringField, FloatField

class AddSnackForm(FlaskForm):
    
    name = StringField('Snack Name')
    price = FloatField('Price in USD')
    quantity = FloatField('Amount of Snack')