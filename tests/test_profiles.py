'''Tests for the profiles directory'''

def test_account_data_manager(client):
    # try route when no user is logged in
    response = client.get('/profiles/account_data', data={})
    assert response.status_code == 302

    # simulate logging in of a user
    response = client.post('/auth/login_pass', data={
        'email': 'testSteve@example.com',
        'password': 'password1234'
        })

    assert response.status_code == 200

    # route when the user is loged in

    response = client.get('/profiles/account_data')
    assert response.status_code == 200 # the route is executed

    assert response.json['userId'] == 2
    assert response.json['userName'] == 'testSteveManager'
    assert response.json['userEmail'] == 'testSteve@example.com'
    assert response.json['userRole'] == 'garage manager'
    assert response.json['userProfilePic'] == None


def test_account_data_driver(client):
    # try route when no user is logged in
    response = client.get('/profiles/account_data', data={})
    assert response.status_code == 302

    # simulate logging in of a user
    response = client.post('/auth/login_pass', data={
        'email': 'testPeter@example.com',
        'password': 'password1234'
        })

    assert response.status_code == 200

    # route when the user is loged in

    response = client.get('/profiles/account_data')
    assert response.status_code == 200 # the route is executed

    assert response.json['userId'] == 1
    assert response.json['userName'] == 'testPeterDriver'
    assert response.json['userEmail'] == 'testPeter@example.com'
    assert response.json['userRole'] == 'driver'
    assert response.json['userProfilePic'] == None


def test_account_data_user(client):
    # try route when no user is logged in
    response = client.get('/profiles/account_data', data={})
    assert response.status_code == 302

    # simulate logging in of a user
    response = client.post('/auth/login_pass', data={
        'email': 'testMike@example.com',
        'password': 'password1234'
        })

    assert response.status_code == 200

    # route when the user is loged in
    
    response = client.get('/profiles/account_data')
    assert response.status_code == 200 # the route is executed

    assert response.json['userId'] == 3
    assert response.json['userName'] == 'testMikeUser'
    assert response.json['userEmail'] == 'testMike@example.com'
    assert response.json['userRole'] == 'user'
    assert response.json['userProfilePic'] == None

def test_account_bus(client):
    '''test for route /profiles/account_bus'''
    # test without login credentials
    response = client.get('/profiles/account_bus')
    assert response.status_code == 302

    # log in driver
    response = client.post('/auth/login_pass', data={
        'email': 'testPeter@example.com',
        'password': 'password1234'
        })
    assert response.status_code == 200

    # check for bus associated with the driver
    response = client.get('/profiles/account_bus')
    assert response.status_code == 200
    assert response.json['busId'] == 'Null'
