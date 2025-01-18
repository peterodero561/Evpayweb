function goBack() {
    window.history.back('passengers_home.html');
}

const prices = {
    multimedia: 30.00,
    downtown: 100.00,
    airport: 150.00,
    cbd: 200
};

document.addEventListener('DOMContentLoaded', function(){
    //add inputs for user to enter their credentials for payment
    const billingMethods = document.querySelectorAll('input[name="billing"]');
    const credentials = document.getElementById('credentials');

    billingMethods.forEach((radio) => {
        radio.addEventListener('change', function(event){
            if (event.target.value === 'mpesa') {
                credentials.style.display = 'block';
            } else {
                credentials.style.display = 'none';
            }
        });
    });
});

function updatePrice() {
    const destination = document.getElementById('destination').value;
    const priceDisplay = document.getElementById('price');
    if (destination in prices) {
        priceDisplay.innerHTML = prices[destination].toFixed(2);
    } else {
        priceDisplay.innerHTML = "0.00";
    }
}

function sendPayment() {
    const selectedBillingMethod = document.querySelector('input[name="billing"]:checked');
    const seatNumber = document.getElementById('seat-number').value;
    const destination = document.getElementById('destination').value;
    const amount = document.getElementById('price').textContent;
    const phone_number = document.getElementById('phone_number').value;

    if (!selectedBillingMethod) {
        alert("Please select a billing method.");
        return;
    }

    if (!destination) {
        alert("Please select a destination.");
        return;
    }

    // calling pay route
    if (selectedBillingMethod.value === 'mpesa') {
        const paymentData = {
            phone_number: phone_number,
            amount: parseFloat(amount),
            seatNumber: seatNumber,
            destination: destination,
        }
        fetch('/payments/pay/', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(paymentData)
        })
        .then (responce => responce.json())
        .then (data => {
            console.log(data);
            alert(data.error);
        })
        .catch(error => {
            console.log(error);
            alert(error);
        });
    }
}