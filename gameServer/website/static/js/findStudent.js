var button = document.getElementById('button-search').addEventListener("click",() => {
    var classInput = document.getElementById('input-class').value
    var roleNumberInput = document.getElementById('input-role-number').value

    if(classInput !== '' && roleNumberInput !== ''){
        location.href = `/dashboard/${classInput}/${roleNumberInput}`
    }
})