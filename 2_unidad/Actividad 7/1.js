function busquedaLineal(arr, elemento) {
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] === elemento) {
            return i;
        }
    }
    return -1;
}

var arregloNumerico = [3, 6, 9, 12, 15, 18];

var elementoBuscado = prompt("Ingresa el número que deseas buscar:");

elementoBuscado = parseInt(elementoBuscado);

var resultado = busquedaLineal(arregloNumerico, elementoBuscado);

if (resultado !== -1) {
    console.log(`El elemento ${elementoBuscado} se encuentra en el índice ${resultado}.`);
} else {
    console.log(`El elemento ${elementoBuscado} no se encuentra en el arreglo.`);
}
