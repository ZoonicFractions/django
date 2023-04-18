document.getElementById('update-user').addEventListener('click', async () => {
    var primary_key = document.getElementById('primary_key').innerHTML
    var username = document.getElementById('username-input').value
    var email = document.getElementById('email-input').value
    var first_name = document.getElementById('firstname-input').value
    var last_name = document.getElementById('lastname-input').value
    var is_staff = document.getElementById('isstaff-input').checked

    var formData = {'primary_key': primary_key, 'username': username,
                    'email': email, 'first_name': first_name, 
                    'last_name': last_name, 'is_staff': is_staff }

    await fetch('/api/update-user', {
        method: 'PUT',
        body: JSON.stringify(formData)
    }).then(() => {
        location.href = document.referrer
    })
})

document.getElementById('eliminate-user').addEventListener('click', async () => {
    var primary_key = document.getElementById('primary_key').innerHTML
    var formData = {'primary_key': primary_key}

    await fetch(`/api/delete-user/${primary_key}`, {
        method: 'DELETE',
        body: formData
    }).then(() => {
        location.href = document.referrer
    })
})