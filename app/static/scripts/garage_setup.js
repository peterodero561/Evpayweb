document.getElementById('garage-setup-form').addEventListener('submit', function (event) {
    event.preventDefault();

    // Get form values
    const garageName = document.getElementById('garage-name').value;
    const garageLocation = document.getElementById('garage-location').value;
    const garageServices = document.getElementsByName("Services");

    //get form data
    const form = document.getElementById('garage-setup-form')
    const formData = new FormData(form);

    fetch('/auth/register_garage', { method: 'POST', body: formData })
    .then(response => response.json())
    .then(data => {
        alert(`${data.message}`)
    })
    .catch(error => alert(`${error}`))

    //services are in a checkbox
    servicesList = [];
    for (const service of garageServices){
        if (service.checked){
            servicesList.push(service.value);
        }
    }
});
