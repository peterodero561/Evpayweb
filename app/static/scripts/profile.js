// load profile data from server
document.addEventListener('DOMContentLoaded', function() {
    fetch_data_user();
});

// function to go to home page
function goBack() {
    window.history.back('passengers_home.html');
}

//function to fetch data from server of current user
function fetch_data_user() {
    fetch('/profiles/account_data', {method: 'GET'})
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (data.userRole === 'driver'){
            fetch_data_bus(function(success){
                if (success === 1) {
                    document.getElementById('edit-bus-btn').style.display = 'inline-block';
                } else {
                    document.getElementById('add-bus-btn').style.display = 'inline-block';
                }
            });
        } else if (data.userRole == 'garage manager') {
            fetch_data_garage(function(success){
                if (success === 1) {
                    document.getElementById('edit-garage-btn').style.display = 'inline-block';
                } else {
                    document.getElementById('add-garage-btn').style.display = 'inline-block';
                }
            });
        }
        document.querySelector('.profile-pic').innerHTML = `
            <img id="profile-image" src="/static/images/profiles/${encodeURIComponent(data.userProfilePic || 'default.jpg')}" alt="Profile Picture">
        `;

        document.querySelector('.profile-info').innerHTML = `
            <h2 style='color: green;'>My Information</h2>
            <p><strong>Name:</strong> <span id="name-display">${data.userName}</span></p>
            <p><strong>Email:</strong> <span id="email-display">${data.userEmail}</span></p>
            <p><strong>Designation:</strong> <span id="designation-display">EV ${data.userRole}</span></p>
        `;
    })
    .catch(error => {
        document.querySelector('.profile-info').innerHTML = `
            <h2>Error ${error}</h2>
        `;
    });
}

//function for fetch data of bus
function fetch_data_bus(callback){
    // fetch bus from server
    fetch('/profiles/account_bus', {method: 'GET'})
    .then(response => {
        console.log('Response', response);
        return response.json()
    })
    .then(data => {
        if (data.busId == "Null") {
            document.querySelector('.update-message').style.display = 'block';
            document.querySelector('.update-message').innerHTML = `
                <h3>You have not registered a bus</h3>
            `;
            // call the call back with zero to indicate failure
            if (callback) callback(0);
        } else {
            document.querySelector('.bus-info').innerHTML = `
                <h2 style='color: green;'>My Bus Information</h2>
                <p><strong>Bus Plate:</strong> <span id="name-display"> ${data.busPlateNo}</span></p>
                <p><strong>Bus Model:</strong> <span id="email-display"> ${data.busModel}</span></p>
                <p><strong>Bus Battery Model:</strong> <span id="designation-display"> ${data.busBatteryModel}</span></p>
                <p><strong>Bus Battery Company:</strong> <span id="designation-display"> ${data.busBatteryCompany}</span></p>
                <p><strong>Bus Battery Seats:</strong> <span id="designation-display"> ${data.busSeatsNo}</span></p>
            `;
            // call the call back with one to indicate success
            if (callback) callback(1);
        }
    })
    .catch(error =>{
        console.error('Error: ', error);
        document.querySelector('.update-message').style.display = 'block';
        document.querySelector('.update-message').innerHTML = `
            <h3>Error Fetching Bus Information</h3>
        `;
        // call the call back with zero to indicate failure
        if (callback) callback(0);
    });
}

//fetch data of garage
function fetch_data_garage(callback){
    fetch('/profiles/account_garage', {method : 'GET'})
    .then(response => response.json())
    .then(data => {
        if (data.garId === 'Null') {
            document.querySelector('.update-message').style.display = 'block';
            document.querySelector('.update-message').innerHTML = `
                <h3>You have not registered a Garage</h3>
            `;
            // call the call back with zero to indicate failure
            if (callback) callback(0);
        } else {
            document.querySelector('.garage-info').innerHTML = `
                <h2 style='color: green;'>My Garage Information</h2>
                <p><strong>Garage Name:</strong><span>${data.garName}</span></p>
                <p><strong>Garage Location:</strong><span>${data.garLocation}</span></p>
                <p><strong>Garage Services:</strong><span>${data.garServices}</span></p>
            `;
            if (callback) callback(1);
        }
    })
    .catch(error => {
        console.error('Error: ', error);
        document.querySelector('.update-message').style.display = 'block';
        document.querySelector('.update-message').innerHTML = `
            <h3>Error Fetching Garage Information</h3>
        `;
        // call the call back with zero to indicate failure
        if (callback) callback(0);
    })
}


// Toggle edit mode
document.getElementById('edit-btn').addEventListener('click', function () {
    document.getElementById('edit-fields').style.display = 'block';
    document.getElementById('edit-btn').style.display = 'none';
    document.getElementById('save-btn').style.display = 'inline-block';
    document.querySelector('.profile-info').style.display = 'none'
    document.querySelector('.profile-pic').style.display = 'none'
    document.getElementById('add-btn').style.display = 'none';
});


// Save the changes and update display
document.getElementById('save-btn').addEventListener('click', function () {

    const form = document.querySelector('.update-form');
    const formData = new FormData(form);
    const newPasswd = document.getElementById('new-password').value;
    const confirmPasswd = document.getElementById('confirm-new-password').value;

    if (newPasswd !== confirmPasswd) {
        document.querySelector('.update-message').style.display = 'block';
        document.querySelector('.update-message').innerHTML = `
            <h2>New Password and Confirm password do not match</h2>
        `;
        document.getElementById('new-password').style.border = '1px solid red';
        document.getElementById('confirm-new-password').style.border = '1px solid red';
    } else {
        // disable save button
        document.getElementById('save-btn').disabled = true;

        fetch('/profiles/account_update', {
            method: 'PUT',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // enable save button
            document.getElementById('save-btn').disabled = false;
            if (data.status === 'success') {
                window.location.href = '/profiles/account'
            } else {
                document.querySelector('.update-message').style.display = 'block';
                document.querySelector('.update-message').innerHTML = `
                    <h2>${data.message}</h2>
                `;
            }
        })
        .catch(error => {
            // enable save button
            document.getElementById('save-btn').disabled = false;
            document.querySelector('.update-message').style.display = 'block';
                document.querySelector('.update-message').innerHTML = `
                    <h2>Error: ${error}</h2>
                `;
        });
    }
});

document.getElementById('add-btn').addEventListener('click', function() {
    document.querySelector('.profile-info').style.display = 'none';
    document.querySelector('.profile-pic').style.display = 'none';
    document.getElementById('edit-btn').style.display = 'none';
    document.getElementById('add-btn').style.display = 'none';

    document.querySelector('#add-bus-form').style.display = 'block';
    document.getElementById('save-bus-btn').style.display = 'inline-block';
});

// listner for save bus button
document.getElementById('save-bus-btn').addEventListener('click', function() {
    document.getElementById('save-bus-btn').disabled = true;
    const form = document.getElementById('add-bus-form');
    const formData = new FormData(form);

    fetch('/auth/register_bus', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.code == 200){
            window.location.href = '/profiles/account';
        } else if (data.code == 403){
            document.querySelector('.update-message').style.display = 'block';
            document.getElementById('save-bus-btn').disabled = false;
            document.querySelector('.update-message').innerHTML = `
                <h2>Error ${data.message}</h2>
            `;
        }
    })
    .catch(error => {
        document.querySelector('.update-message').style.display = 'block';
        document.getElementById('save-bus-btn').disabled = false;
        document.querySelector('.update-message').innerHTML = `
            <h2>Error ${error}</h2>
        `;
    });
});

//event listener for the edit bus button
document.getElementById('edit-bus-btn').addEventListener('click', function() {
    document.querySelector('.profile-info').style.display = 'none';
    document.querySelector('.profile-pic').style.display = 'none';
    document.getElementById('edit-btn').style.display = 'none';
    document.getElementById('edit-bus-btn').style.display = 'none';

    document.getElementById('add-bus-form').style.display = 'block';
    document.getElementById('save-edit-bus-btn').style.display = 'inline-block';
});

// event listners to add listner to the save-edit bus button
document.getElementById('save-edit-bus-btn').addEventListener('click', function(){
    document.getElementById('save-edit-bus-btn').disabled = true;
    const form = document.getElementById('add-bus-form');
    const formData = new FormData(form);

    fetch('/profiles/account_bus_update', {
        method: 'PUT',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.code == 200){
            window.location.href = '/profiles/account';
        } else if (data.code == 403){
            document.querySelector('.update-message').style.display = 'block';
            document.getElementById('save-bus-btn').disabled = false;
            document.querySelector('.update-message').innerHTML = `
                <h2>Error ${data.message}</h2>
            `;
        }
    })
    .catch(error => {
        document.querySelector('.update-message').style.display = 'block';
        document.getElementById('save-bus-btn').disabled = false;
        document.querySelector('.update-message').innerHTML = `
            <h2>Error ${error}</h2>
        `;
    });
});