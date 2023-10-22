from flask import Flask, request, render_template,  redirect, flash, session, url_for
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import URL, Optional
from models import connect_db, db, Pet
from flask_wtf import FlaskForm
from forms import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:SmokingPot420@localhost/adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "darknight"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

@app.route('/')
def homepage():
    """Render home page"""

    pets = db.session.query(Pet).all()
    return render_template("home.html", pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """ Route for adding a pet"""

    form = AddPetForm()
    if form.validate_on_submit():
        pet = Pet(
            name= form.name.data,
            species= form.species.data,
            photo_url= form.photo_url.data,
            age= form.age.data,
            notes= form.notes.data,
            available= form.available.data
        )
        db.session.add(pet)
        db.session.commit()
        
        flash('Pet Added', 'success')
        return redirect(url_for('homepage'))
    return render_template("add_pet.html", form=form)

@app.route('/<int:pet_id>)', methods=['GET', 'POST'])
def pet_detail(pet_id):
    pet = Pet.query.get(pet_id)
    if pet is None:
        flash('Pet not found', 'danger')
        return redirect(url_for('homepage'))
    
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        form.populate_obj(pet)
        db.session.commit()
        flash('Pet details updated successfully', 'success')
        return redirect(url_for('homepage'))
    
    return render_template('pet_detail.html', pet=pet, form=form)

class EditPetForm(FlaskForm):
    photo_url = StringField('photo', validators=[Optional(), URL()])
    notes = TextAreaField('notes')
    available = BooleanField('available')