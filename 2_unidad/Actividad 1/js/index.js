// Obtener una referencia al botón y al párrafo
const botonSaludo = document.getElementById('boton-saludo');
const mensajeSaludo = document.getElementById('mensaje-saludo');

// Agregar un evento click al botón
botonSaludo.addEventListener('click', function () {
    // Cambiar el texto del párrafo al hacer clic en el botón
    mensajeSaludo.textContent = '¡Hola, mundo!';
});
