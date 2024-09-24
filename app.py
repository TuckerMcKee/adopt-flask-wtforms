from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetsForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['DEBUG'] = True
debug = DebugToolbarExtension(app)

connect_db(app)
with app.app_context():
    db.create_all()

@app.route('/')
def pet_listing():
    """display list of pets"""
    pets = Pet.query.all()
    return render_template("petlisting.html",pets=pets)
    
@app.route('/add',methods=["GET","POST"])
def add_pet():
    """show form for adding pets/process form data""" 
    form = AddPetsForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        image_url = form.image_url.data
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(name=name,species=species,image_url=image_url,age=age,notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:    
        return render_template("addpetform.html",form=form)
    
@app.route('/<int:pet_id>',methods=["GET","POST"])
def pet_info(pet_id):
    """diplay pet data and form for editing pet data/process data on form submit"""  
    pet = db.session.get(Pet,pet_id) 
    form = AddPetsForm(obj=pet) 
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.image_url = form.image_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        db.session.commit()
        flash(f"Updated info for Pet ID:{pet.id}")
        return redirect('/')
    else:
        return render_template('petinfo.html',pet=pet,form=form)
