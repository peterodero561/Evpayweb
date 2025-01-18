document.getElementById('stationForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const password = document.getElementById('userPassword').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    
    if (password !== confirmPassword) {
        alert('Passwords do not match!');
        return;
    }
    
    alert('Station setup finalized!');
});
