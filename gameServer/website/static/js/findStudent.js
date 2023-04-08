document.getElementById('button-search').addEventListener("click",() => {
    var classInput = document.getElementById('input-class').value
    var roleNumberInput = document.getElementById('input-role-number').value

    if(classInput !== '' && roleNumberInput !== ''){
        fetch(`/api/view-logs-student/${classInput.toUpperCase()}/${roleNumberInput}`)
        .then(response => response.json())
        .then(data => {
            if (data.status == 'success') {
                location.href = `${classInput.toUpperCase()}/${roleNumberInput}`
            } else{
                location.href = `/notfound`
            }
        })
    }
})