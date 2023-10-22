from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import InputRequired, URL, Optional, AnyOf,  NumberRange

class AddPetForm(FlaskForm):
    name= StringField('Name', validators=[InputRequired()])
    species= StringField('Species', validators=[InputRequired(), AnyOf(['cat', 'dog', 'porcupine'])])
    photo_url= StringField('Photo', validators=[URL()])
    age= IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30)])
    notes= TextAreaField('Notes')
    available= BooleanField('Available')
