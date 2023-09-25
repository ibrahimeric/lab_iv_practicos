// 2.	Actividad de Funciones, arreglos y validación de formularios en JavaScript:
// •	Desarrolla una función en JavaScript que tome como parámetro una lista de números y devuelva la suma de todos los elementos.

function operaciones(cantidad) {
    var nuevoArray = [];
    count = 1
    while (count <= cantidad){
        nuevoArray[count -1] = parseFloat(prompt("Introduce un numero:", ""))
        count++;
    }
    count = 1
    suma = 0
    while (count <= nuevoArray.length){
        suma = suma + nuevoArray[count -1]
        count++;
    }
    console.log("La suma de todos los numeros ingresados es: ", suma)
}

operaciones(parseFloat(prompt("¿Cuantos numeros deseas sumar?", "")))