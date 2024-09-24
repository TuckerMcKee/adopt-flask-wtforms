from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """model for pets table"""
    __tablename__ = 'pets'

    def __repr__(self):
        return f"<id={self.id} name={self.name} species={self.species} image_url={self.image_url} age={self.age} available={self.available}"

        
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text,nullable=False)
    image_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, default=True)

  
        
