document.getElementById('button-search').addEventListener("click",() => {
    var classInput = document.getElementById('input-class').value
    var roleNumberInput = document.getElementById('input-role-number').value
    var difficultyInput = document.getElementById('input-difficulty').value

    if(classInput !== '' && roleNumberInput !== '' && difficultyInput != ''){
        fetch(`/api/view-logs-student/${difficultyInput}/${classInput.toUpperCase()}/${roleNumberInput}`)
        .then(response => response.json())
        .then(data => {
            if (data.status == 'success') {
                location.href = `/dash/${difficultyInput}/${classInput.toUpperCase()}/${roleNumberInput}`
            } else{
                location.href = `/dash/notfound`
            }
        })
    }
})