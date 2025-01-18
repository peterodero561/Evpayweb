from app.extensions import db
from flask_login import UserMixin
'''class for the User'''


class User(UserMixin, db.Model):
    '''class to create the user table in evpay_db'''
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    user_email = db.Column(db.String(50), nullable=False, unique=True)
    user_password = db.Column(db.String(255), nullable=False)
    user_role = db.Column(db.String(20), nullable=True)
    user_profile_pic = db.Column(db.String(100), nullable=True)

    def __init__(self, id=None, name=None, email=None, passwd=None, role=None, pic=None):
        '''function to initialize the class'''
        self.user_id = id
        self.user_name = name
        self.user_email = email
        self.user_role = role
        self.user_password = passwd
        self.user_profile_pic = pic

    def __repr__(self):
        '''function to specifie what to print if class is called'''
        return f'Passenger(passName: {self.pass_name})'
    
    def to_dict(self):
        '''function to return dictionary format of the class'''
        return {
            'userId': self.user_id,
            'userName': self.user_name,
            'userEmail': self.user_email,
            'userRole': self.user_role,
            'userProfilePic': self.user_profile_pic
        }

    def get_id(self):
        '''returns user_id for the flask login'''
        return self.user_id
