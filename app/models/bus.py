from flask_sqlalchemy import SQLAlchemy
from app.extensions import db

class Bus(db.Model):
    __tablename__ = 'buses'
    busId = db.Column(db.Integer, primary_key=True)
    busModel = db.Column(db.String(50), nullable=False)
    busPlateNo = db.Column(db.String(50), nullable=False, unique=True)
    busBatteryModel = db.Column(db.String(50), nullable=False)
    busBatteryComapny = db.Column(db.String(50), nullable=False)
    busSeatsNo = db.Column(db.Integer, nullable=False)
    # Foreign key linking to Driver model, referenced as a string
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.driver_id'), nullable=False)


    def __init__(self, model=None, plate=None, battery_model=None, battery_company=None, seatsNo=None, driverId=None, id=None):
        self.busId = id
        self.busModel = model
        self.busPlateNo = plate
        self.busBatteryModel= battery_model
        self.busBatteryComapny = battery_company
        self.busSeatsNo = seatsNo
        self.driver_id = driverId

    def __repr__(self):
        return f'Bus(busPlate: {self.busPlateNo}, busModel: {self.busModel}, busDriverName: {self.driver.driverName})'
    
    def to_dict(self):
        return {
            'busId': self.busId,
            'busModel': self.busModel,
            'busPlateNo': self.busPlateNo,
            'busBatteryModel': self.busBatteryModel,
            'busBatteryCompany': self.busBatteryComapny,
            'busSeatsNo': self.busSeatsNo,
            'busDriveId': self.driver_id
        }
