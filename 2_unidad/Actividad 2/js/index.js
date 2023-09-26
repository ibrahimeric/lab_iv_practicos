// Obtener una referencia al botón y al párrafo
const botonSaludo = document.getElementById('botonSaludo');
const mensajeSaludo = document.getElementById('mensajeSaludo');

// Agregar un evento click al botón
botonSaludo.addEventListener('click', function () {
    // Cambiar el texto del párrafo al hacer clic en el botón
    mensajeSaludo.textContent = '¡Hola, mundo!';
});
