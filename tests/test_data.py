'''Adds data to the test database to help with testing routes
that require session'''

from app.models.user import User
from app.models.driver import Driver
from app.models.garage_manager import GarageManager
from app.models.bus import Bus
from app.models.garage import Garage
from app.extensions import db
from werkzeug.security import generate_password_hash


def setup_test_data():
    '''Adds data to the test database to help with testing routes
    that require session'''
    db.create_all()
    user_driver = User(
            email='testPeter@example.com',
            passwd=generate_password_hash('password1234'),
            name='testPeterDriver',
            role='driver',
            id=1
            )
#     user_bus = User(
#         email='testBusDriver@example.com',
#         passwd=generate_password_hash('password1234'),
#         name='testBusDriver',
#         role='driver',
#         id=4
#     )
    user_garage_manager = User(
            email='testSteve@example.com',
            name='testSteveManager',
            passwd=generate_password_hash('password1234'),
            role='garage manager',
            id=2
            )
#     user_garage = User(
#         email='testGarageManager@example.com',
#         name='testGarageManager',
#         passwd=generate_password_hash('password1234'),
#         role='garage manager',
#         id=5
#   )
    user = User(
            email='testMike@example.com',
            passwd=generate_password_hash('password1234'),
            name='testMikeUser',
            role='user',
            id=3
            )

    db.session.add(user_driver)
#     db.session.add(user_bus)
#     db.session.add(user_garage)
    db.session.add(user_garage_manager)
    db.session.add(user)
    db.session.commit()

    driver = Driver(
        email='testPeter@example.com',
        passwd=generate_password_hash('password1234'),
        name='testPeterDriver',
        number='0742325257',
        user_id=1,
    )

#     driver_bus = Driver(
#         email='testBusDriver@example.com',
#         passwd=generate_password_hash('password1234'),
#         name='testBusDriver',
#         number='0742325257',
#         user_id=4,
#         driver_id=2
#     )

    garage_manager = GarageManager(
            name='testSteveManager',
            email='testSteve@example.com',
            number='0742325257',
            user_id=2,
            )
    
#     manage_garage = GarageManager(
#         email='testGarageManager@example.com',
#         name='testGarageManager',
#         passwd=generate_password_hash('password1234'),
#         number='0742325257',
#         user_id=5,
#         id=2
#     )
    

    db.session.add(driver)
    db.session.add(garage_manager)
#     db.session.add(manage_garage)
#     db.session.add(driver_bus)
    db.session.commit()

#     test_garage = Garage(
#         garName='testGarage',
#         garLocation='testLocation',
#         garServices='testServices',
#         managerId=2
#     )

#     test_bus = Bus(
#         model='testModel',
#         plate='testPlate',
#         battery_model='testBatteryModel',
#         battery_company='testBatteryCompany',
#         seatsNo=42,
#         driverId=2
#     )

#     db.session.add(test_bus)
#     db.session.add(test_garage)
#     db.session.commit()