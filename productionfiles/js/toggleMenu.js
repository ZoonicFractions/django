var paragraphs = document.getElementsByClassName('sidebar-menu-paragraph')
paragraphs = [].slice.call(paragraphs);

paragraphs.map((x) => {

    x.onclick = () => {
        var menu = document.getElementsByClassName('toggle-menu')

        if(menu[x.id].style.display == 'none'){
            menu[x.id].style.display = 'flex'
        }else{
            menu[x.id].style.display = 'none'
        }
    }
})