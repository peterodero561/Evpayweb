function goBack() {
    window.history.back('passengers_home.html');
}

function topUpBalance() {
    alert("Top Up Balance button clicked!");
    // Add the logic for topping up the balance
}

function payWithBalance() {
    alert("Pay button clicked!");
    // Add the logic for paying with the EV balance
}

document.addEventListener('DOMContentLoaded', function() {
    fetch_account_data();
});

function fetch_account_data() {
    fetch('/profiles/account_data', {method: 'GET'})
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok: ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        document.querySelector('.account-section').innerHTML = `
            <h2 class="section-title">Account Information</h2>
            <p><strong>Account Type:</strong> EV ${data.user_role}</p>
            <p><strong>Name:</strong> ${data.user_name}</p>
            <p><strong>Email:</strong> ${data.user_email}</p>
        `;
    })
    .catch(error => {
        document.querySelector('.account-section').innerHTML = `
            <h2 class='section-title'> Error fetching account information<\h2>
        `;
        console.error('Fetch error:', error);
    });
}