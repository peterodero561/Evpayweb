document.querySelector('.login-btn').addEventListener('click', () => {
    window.location.href = '/auth/login';
});

document.querySelector('.google-login-btn').addEventListener('click', () => {
    alert('Google login functionality here.');
});

document.addEventListener('DOMContentLoaded', function() {

    const account = document.getElementById('account-type');
    const phoneField = document.getElementById('phone-field');
    const form = document.getElementById('signup-form');
    const responseMessage = document.getElementById('response-message');

    account.addEventListener('change', function(event) {
        const option = event.target.value;

        if (option === 'user') {
            phoneField.style.display = 'none';
            responseMessage.style.display = 'none';
            form.action = '/auth/register_user';
        } else if (option === 'driver') {
            phoneField.style.display = 'block';
            responseMessage.style.display = 'none';
            form.action = '/auth/register_driver';
        } else if (option === 'garage_manager') {
            phoneField.style.display = 'block';
            responseMessage.style.display = 'none';
            form.action = '/auth/register_manager';
        } else if (option === '') {
            responseMessage.style.display = 'block';
            responseMessage.textContent = 'Please select an Account Type';
            responseMessage.style.color = 'red';
            return;
        }
    });

    // forwarding data to server side
    form.addEventListener('submit', function(event) {
        event.preventDefault();

        // get form data
        const formData = new FormData(form);
        fetch(form.action, {method: 'POST', body: formData})
        .then(response => response.json())
        .then(data => {
            responseMessage.style.display = 'block';
            responseMessage.textContent = data.message || 'Registration sucessful';
            responseMessage.className = data.status === 'error'? 'error': 'success';
        })
        .catch(error => {
            responseMessage.style.display = 'block';
            responseMessage.textContent = 'An error occured' + error.message;
            responseMessage.className = 'error';
        });
    });
});