document.getElementById('button-search').addEventListener("click",() => {
    var classInput = document.getElementById('input-class-phone').value
    var roleNumberInput = document.getElementById('input-role-number-phone').value
    var difficultyInput = document.getElementById('input-difficulty-phone').value

    if(classInput !== '' && roleNumberInput !== '' && difficultyInput != ''){
        fetch(`/api/view-logs-student/${difficultyInput}/${classInput.toUpperCase()}/${roleNumberInput}`)
        .then(response => response.json())
        .then(data => {
            if (data.status == 'success') {
                location.href = `/${difficultyInput}/${classInput.toUpperCase()}/${roleNumberInput}`
            } else{
                location.href = `/notfound`
            }
        })
    }
})