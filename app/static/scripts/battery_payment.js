function sendPayment() {
    const selectedBillingMethod = document.querySelector('input[name="billing"]:checked');
    if (!selectedBillingMethod) {
        alert("Please select a billing method.");
        return;
    }

    // Here, you can add logic to handle the payment processing using the selected billing method
    alert(`Payment sent using ${selectedBillingMethod.value}`);
}

function refundPayment() {
    // Logic to handle refunds
    alert("Refund initiated.");
}

function goBack() {
    window.history.back('owners_home.html');
}