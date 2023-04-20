var potentials = document.querySelectorAll("[class^=progress-bar]")

potentials.forEach((x) => {
    // Getting the value
    var className = x.className
    var position = className.match("progress-bar \?(.*)")[1]

    x.style.backgroundPosition = '-' + position + '%'

    // Changing the color given the grade
    var colorArray = ['rgb(238, 71, 43)', 'rgb(243, 144, 21)', 'rgb(252, 224, 31)', 'rgb(205, 234, 74)', 'rgb(95, 218, 113)']
    position = parseFloat(position)
    var positionComplement = 100 - position
    if(position >= 0 && position <= 42){
        x.style.backgroundImage = `linear-gradient(90deg, #ccc 50%, ${colorArray[0]} 50%)`;
    }else if(position > 42 && position <= 62){
        x.style.backgroundImage = `linear-gradient(90deg, #ccc 50%, ${colorArray[1]} 50%)`;
    }else if(position > 62 && position <= 72){
        x.style.backgroundImage = `linear-gradient(90deg, #ccc 50%, ${colorArray[2]} 50%)`;
    }else if(position > 72 && position <= 82){
        x.style.backgroundImage = `linear-gradient(90deg, #ccc 50%, ${colorArray[3]} 50%)`;
    }else if(position > 82 && position <= 100){
        x.style.backgroundImage = `linear-gradient(90deg, #ccc 50%, ${colorArray[4]} 50%)`;
    }
})