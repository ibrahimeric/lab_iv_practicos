// Desarrolla una función en JavaScript que tome como parámetro una lista de números y devuelva 
// la suma de todos los elementos.

function sumaDeElementos(listaDeNumeros) {
  let suma = 0;
  for (let i = 0; i < listaDeNumeros.length; i++) {
    suma += parseFloat(listaDeNumeros[i]); // Usamos parseFloat para asegurar que los valores sean números.
  }
  return suma;
}

// Ejemplo de uso en la consola de Node.js
const numeros = [1, 2, 3, 4, 5];
const resultado = sumaDeElementos(numeros);

console.log(`La suma de los números es: ${resultado}`);

