function ordenamientoBurbuja(arr) {
    var n = arr.length;
    var intercambiado;
    do {
        intercambiado = false;
        for (var i = 0; i < n - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                var temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
                intercambiado = true;
            }
        }
    } while (intercambiado);

    return arr;
}

var arregloNumerico = [64, 34, 25, 12, 22, 11, 90];
console.log("Arreglo antes de ordenar:", arregloNumerico);

ordenamientoBurbuja(arregloNumerico);

console.log("Arreglo después de ordenar:", arregloNumerico);
