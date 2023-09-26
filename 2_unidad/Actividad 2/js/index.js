// Función para validar el formulario antes de enviar
function validarFormulario(event) {
    event.preventDefault(); // Prevenir la acción predeterminada del formulario (evitar que se envíe)

    // Obtener los valores de los campos del formulario
    const nombre = document.getElementById('nombre').value; // Obtener el valor del campo "nombre"
    const email = document.getElementById('email').value; // Obtener el valor del campo "email"
    const contrasena = document.getElementById('contrasena').value; // Obtener el valor del campo "contrasena"
    const mensaje = document.getElementById('mensaje').value; // Obtener el valor del campo "mensaje"

    // Realizar validación
    if (nombre === '' || email === '' || contrasena === '' || mensaje === '') {
        // Si alguno de los campos está vacío, muestra una alerta al usuario
        alert('Por favor, llene todos los campos antes de enviar.');
    } else {
        // Si todos los campos están completos, puedes realizar acciones adicionales aquí
        // Por ejemplo, enviar los datos al servidor si lo deseas
        alert('Formulario enviado con éxito.');
        // Aquí puedes agregar código para enviar los datos al servidor
    }
}

// Agregar un evento para el envío del formulario
const formulario = document.querySelector('.contact-form'); // Selecciona el formulario por su clase
formulario.addEventListener('submit', validarFormulario); // Agrega un evento "submit" y llama a la función validarFormulario cuando se envía el formulario
