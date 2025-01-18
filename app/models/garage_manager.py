from flask_sqlalchemy import SQLAlchemy
from app.extensions import db
from app.models.garage import Garage
'''Class for table GarageManager in database'''

class GarageManager(db.Model):
    '''Table garManagers'''
    __tablename__ = 'garManagers'
    managerId = db.Column(db.Integer, primary_key = True)
    managerName = db.Column(db.String(50), nullable=False)
    managerEmail = db.Column(db.String(50), nullable=False)
    managerNo = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    garages = db.relationship('Garage', backref='garage_manager', lazy=True)

    def __init__(self, name, email, number, user_id, id=None):
        '''Method to initialize the class'''
        self.managerName = name
        self.managerId = id
        self.managerEmail = email
        self.managerNo = number
        self.user_id = user_id

    def __repr__(self):
        """String representation of the GarageManager class"""
        return f'Garage Manager {self.managerName}'
    
    def to_dict(self):
        '''Function to return the dictionary format of the given manager'''
        return {
            'garage_manager_id': self.managerId,
            'garage_manager_name': self.managerName,
            'garage_manager_email': self.managerEmail,
            'garage_manager_number': self.managerNo
        }