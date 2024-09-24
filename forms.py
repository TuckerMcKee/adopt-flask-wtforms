from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import URL, NumberRange, Optional

class AddPetsForm(FlaskForm):
    """form for adding pets"""

    name = StringField("Pet Name")
    species = SelectField("Species", choices=[('cat','Cat'),('dog','Dog'),('porcupine','Porcupine')])
    image_url = StringField("Image URL", validators=[Optional(),URL()])
    age = IntegerField("Age", validators=[Optional(),NumberRange(min=0,max=30)])
    notes = StringField("Notes")
    
