// Querring server side for login
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('login-form');
    const responseMessage = document.getElementById('response-message');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        // fetch data from form
        const formData = new FormData(form);

        //send data to server
        fetch('/auth/login_pass', {method: 'POST', body: formData})
        .then(response => response.json())
        .then(data => {
            responseMessage.style.display = 'block';
            responseMessage.textContent = data.message;
            responseMessage.className = data.status === 'error'? 'error': 'success';

            if (data.message === 'Logged in successfully!') {
                //select which home page to serve
                if (data.role == 'user') {
                    window.location.href = '/profiles/user_profile';
                } else if (data.role == 'driver') {
                    window.location.href = '/profiles/driver_profile';
                } else if (data.role == 'garage manager') {
                    window.location.href = '/profiles/manager_profile'
                } else {
                    responseMessage.textContent = 'There was an error creating your account. Please create a new account';
                }
            }
        })
        .catch(error => {
            responseMessage.style.display = 'block';
            responseMessage.textContent = 'An error occured' + error.message;
            responseMessage.className = 'error';
        });
    });
});

// Handle Google login button click
document.querySelector('.google-login-btn').addEventListener('click', () => {
    alert('Google login functionality here.');
});

// Handles create account button click
document.querySelector('.create-account-btn').addEventListener('click', () => {
    window.location.href = '/auth/register';
});
