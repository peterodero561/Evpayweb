'''tests for auth directory'''
from app.models.user import User


def test_register_user(client):
    '''tests for registering a user'''
    # Normal url
    response = client.post('/auth/register_user', data={
        'name': 'testUser',
        'email': 'testUser@example.com',
        'password': 'password1234'
        })

    assert response.status_code == 200
    assert b'You have successfully registered. Procced to Sign In' in response.data

    # when same data
    response = client.post('/auth/register_user', data={
        'name': 'testUser',
        'email': 'testUser@example.com',
        'password': 'password1234'
        })

    assert response.status_code == 403
    assert b'An account with this email already exists' in response.data

    # when url has no data passed
    response = client.post('/auth/register_user', data={})
    assert response.status_code == 400
    assert b'Missing important important details' in response.data

    # when url is missing important details
    response = client.post('/auth/register_user', data={
        'name': 'testUser2',
        'email': 'testUser2@example.com'
        })
    assert response.status_code == 400
    assert b'Missing important important details' in response.data

    # invalid email
    response = client.post('/auth/register_user', data={
        'name': 'testUser2',
        'email': 'testUserexamplecom',
        'password': 'password1234'
        })
    assert response.status_code == 403
    assert b'Invalid email address!' in response.data

    # invalid character name
    response = client.post('/auth/register_user', data={
        'name': '#testUser2',
        'email': 'testUser2@example.com',
        'password': 'password1234'
        })
    assert response.status_code == 403
    assert b'Name must contain only characters and numbers!' in response.data


def test_register_driver(client):
    '''tests registration of driver'''
    response = client.post('/auth/register_driver', data={
        'name': 'testDriver',
        'email': 'testDriver@example.com',
        'password': 'password1234',
        'number': '0742325257'
        })

    assert response.status_code == 200
    assert b'You have successfully registered. Procced to Sign In' in response.data

    # when  data is missing phone number
    response = client.post('/auth/register_driver', data={
        'name': 'testDriver2',
        'email': 'testDriver2@example.com',
        'password': 'password1234'
        })

    assert response.status_code == 400
    assert b'Missing phone number' in response.data


def test_register_garage_manager(client):
    '''tests registration of grage manager'''
    response = client.post('/auth/register_manager', data={
        'name': 'testManager',
        'email': 'testManager@example.com',
        'password': 'password1234',
        'number': '0742325257'
        })

    assert response.status_code == 200
    assert b'You have successfully registered. Procced to Sign In' in response.data

    # when data is missing phone number
    response = client.post('/auth/register_manager', data={
        'name': 'testManager',
        'email': 'testManager@example.com',
        'password': 'password1234'
        })

    assert response.status_code == 400
    assert b'Missing phone number' in response.data


def test_register_bus(client):
    '''tests for registration of buses'''
    # when no driver is logged in
    response = client.post('/auth/register_bus', data={})

    assert response.status_code == 302

    # simulate logging in of a driver
    user = User.query.filter_by(user_email='testPeter@example.com').first()
    assert user is not None, "Test user does not exist in the database"

    # Log in the user using the test client by POSTing to the login endpoint
    response = client.post('/auth/login_pass', data={
        'email': 'testPeter@example.com',
        'password': 'password1234'
    })

    assert response.status_code == 200

    # Normal url
    response = client.post('/auth/register_bus', data={
        'busModel': 'test_model',
        'plate': 'test_plate',
        'batteryModel': 'test_battery_model',
        'batteryCompany': 'test_battery_company',
        'busSeats': '12'
        })

    assert response.status_code == 200
    assert b'Sucessfully Added bus' in response.data

    # when url has already existing data
    response = client.post('/auth/register_bus', data={
        'busModel': 'test_model',
        'plate': 'test_plate',
        'batteryModel': 'test_battery_model',
        'batteryCompany': 'test_battery_company',
        'busSeats': '12'
        })

    assert response.status_code == 403
    assert b'A bus with this Plate Number already exists' in response.data

    # when url is missing data
    response = client.post('/auth/register_bus', data={})

    assert response.status_code == 403
    assert b'Missing important details' in response.data


def test_register_garage(client):
    '''tests for registration of garages'''
    # normal url b4 login
    response = client.post('/auth/register_garage', data={
        'garage-location': 'test_location',
        'garage-name': 'test_name',
        'Services': 'test_services',
        })

    assert response.status_code == 302

    # check if user exists
    user = User.query.filter_by(user_email='testSteve@example.com').first()
    assert user is not None, "Test user does not exist in the database"
    # simulate login
    response = client.post('/auth/login_pass', data={
        'email': 'testSteve@example.com',
        'password': 'password1234'
        })

    assert response.status_code == 200

    # normal url with user manager logged in
    response = client.post('/auth/register_garage', data={
        'garage-location': 'test_location',
        'garage-name': 'test_name',
        'Services': 'test_services',
        })

    assert response.status_code == 200
    assert b'Garage created successfully' in response.data

    # when url has data existing
    response = client.post('/auth/register_garage', data={
        'garage-location': 'test_location',
        'garage-name': 'test_name',
        'Services': 'test_services',
        })

    assert response.status_code == 403

    # when url is missing data
    response = client.post('/auth/register_garage', data={})

    assert response.status_code == 403
    assert b'Missing important details' in response.data
