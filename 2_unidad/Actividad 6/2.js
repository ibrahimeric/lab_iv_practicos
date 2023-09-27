// Definir un diccionario de productos
var productos = [
    {
        nombre: "Producto 1",
        precio: 19.99,
        cantidad: 50
    },
    {
        nombre: "Producto 2",
        precio: 29.99,
        cantidad: 30
    },
    {
        nombre: "Producto 3",
        precio: 9.99,
        cantidad: 100
    }
];

// Función para mostrar la información de un producto específico
function mostrarProducto() {
    var productoSelect = document.getElementById("productoSelect");
    var productoIndex = productoSelect.value;
    var producto = productos[productoIndex];
    var productoInfoDiv = document.getElementById("productoInfo");
    productoInfoDiv.innerHTML = `
        <h2>${producto.nombre}</h2>
        <p>Precio: $${producto.precio.toFixed(2)}</p>
        <p>Cantidad en stock: ${producto.cantidad}</p>
    `;
}

// Agregar un evento de cambio a la lista desplegable
var productoSelect = document.getElementById("productoSelect");
productoSelect.addEventListener("change", mostrarProducto);

// Mostrar la información del producto seleccionado al cargar la página
mostrarProducto();
