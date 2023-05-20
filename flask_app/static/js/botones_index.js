function mostrarCarros(order) {
    var carrosBlocks = document.getElementsByClassName('carros-block');
    
    for (var i = 0; i < carrosBlocks.length; i++) {
    carrosBlocks[i].classList.remove('show');
    }

    var selectedBlock = document.querySelector('.carros-block.' + order);
    selectedBlock.classList.add('show');
}