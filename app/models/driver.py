from flask_sqlalchemy import SQLAlchemy
from app.extensions import db
from app.models.bus import Bus 
'''code for class Driver'''
class Driver(db.Model):
    '''Class for creating the driver table in evpay_db'''
    __tablename__ = 'drivers'
    driver_id = db.Column(db.Integer, primary_key=True)
    driver_no = db.Column(db.String(20), nullable=True)
    driver_name = db.Column(db.String(50), nullable=False)
    driver_email = db.Column(db.String(50), nullable=False, unique=True)
    driver_password = db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    buses = db.relationship('Bus', backref='driver', lazy=True)

    def __init__(self, name, email, number, user_id, passwd, driver_id=None):
        '''function to intialize class Driver'''
        self.driver_id = driver_id
        self.driver_email = email
        self.driver_name = name
        self.driver_password = passwd
        self.driver_no = number
        self.user_id = user_id

    def __repr__(self):
        '''function for the string representation of the Driver class'''
        return f'Driver(driverName:{self.drive_name})'
    
    def to_dict(self):
        '''function to return dictionary format of the driver instance'''
        return {
            'driverId': self.drive_id,
            'driverName': self.driver_name,
            'driverEmail': self.driver_email,
            'driverNumber': self.driver_no,
            'userId': self.user_id
        }
