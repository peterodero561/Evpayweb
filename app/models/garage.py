from flask_sqlalchemy import SQLAlchemy
import json
from app.extensions import db

class Garage(db.Model):
    __tablename__ = 'garages'
    garId = db.Column(db.Integer, primary_key=True)
    garName = db.Column(db.String(50), nullable=False, unique=True)
    garLocation = db.Column(db.String(250), nullable=False, unique=True)
    garServices = db.Column(db.Text, nullable=True)
    # refrence to manager
    managerId = db.Column(db.Integer, db.ForeignKey('garManagers.managerId'), nullable=False)

    def __init__(self, id=None, garName=None, garLocation=None, garServices=None, managerId=None):
        self.garId = id
        self.garName = garName
        self.garLocation = garLocation
        self.garServices = json.dumps(garServices)
        self.managerId = managerId

    def __repr__(self):
        return f'Garage(garageName={self.garName})'
    
    def to_dict(self):
        return {
            'garId': self.garId,
            'garName': self.garName,
            'garLocation': self.garLocation,
            'garServices': json.loads(self.garServices),
            'garManagerId': self.managerId
        }