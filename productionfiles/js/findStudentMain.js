document.getElementById('button-search-main').addEventListener("click",() => {
    var classInput = document.getElementById('input-class-main').value
    var roleNumberInput = document.getElementById('input-role-number-main').value
    var difficultyInput = document.getElementById('input-difficulty-main').value

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