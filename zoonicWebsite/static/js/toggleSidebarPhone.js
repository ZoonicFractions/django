var button = document.querySelectorAll('.phone-toggle');
var mainContent = document.querySelectorAll('.main-content')[0];

button.forEach((object) => {
    object.addEventListener('click', () => {
        var sidebar = document.getElementsByClassName('sidebar-phone')[0];
        console.log(sidebar.className)

        if(sidebar.classList.contains('show-sidebar')){
            sidebar.classList.remove('show-sidebar');
            mainContent.classList.remove('main-content-blur')
        }else{
            sidebar.classList.add('show-sidebar');
            mainContent.classList.add('main-content-blur')
        }
    })
});