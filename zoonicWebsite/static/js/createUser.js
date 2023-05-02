document.getElementById('create-user').addEventListener('click', async () => {
    var username = document.getElementById('username-input').value
    var email = document.getElementById('email-input').value
    var first_name = document.getElementById('firstname-input').value
    var last_name = document.getElementById('lastname-input').value
    var password = document.getElementById('password-input').value
    var is_staff = document.getElementById('isstaff-input').checked
    var classroom = document.getElementById('classroom-input').value

    var formData = {'username': username, 'email': email, 
                    'first_name': first_name, 'last_name': last_name, 
                    'password':password, 'is_staff': is_staff,
                    'classroom': classroom }

    await fetch('/api/create-user', {
        method: 'POST',
        body: JSON.stringify(formData)
    }).then(() => {
        location.href = document.referrer
    })
})