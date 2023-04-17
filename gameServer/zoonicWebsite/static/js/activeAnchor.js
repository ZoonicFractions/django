var anchors = document.querySelectorAll('.sidebar-menu a');
anchors = [].slice.call(anchors);

anchors.map((x) => {
    x.addEventListener('click', () => {
        anchors.map((x) => {
            x.className = 'none'
        })
        x.className = 'active'
    })
})