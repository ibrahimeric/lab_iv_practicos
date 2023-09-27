/* Optimiza el rendimiento de un bucle en JavaScript 
utilizando técnicas como la reducción de operaciones innecesarias. */

/* Versión inicial del código con un bucle for para sumar todos los elementos del array. */

/*
const numbers = [1, 2, 3, 4, 5];
let sum = 0;

for (let i = 0; i < numbers.length; i++) {
  sum += numbers[i];
}

console.log(sum);
*/

/* ------------------------------------------------------ */

// Version optimizada:

const numbers = [1, 2, 3, 4, 5];
let sum = 0;

// Usar un bucle for...of en lugar de for
for (const number of numbers) {
  sum += number;
}

console.log(sum);

// En este ejemplo, hemos aplicado las siguientes optimizaciones:
// Hemos reemplazado el bucle for tradicional con un bucle for...of, lo que hace que el código sea más legible y eficiente.
// Hemos eliminado la necesidad de usar una variable i para mantener el índice actual y hemos accedido directamente a cada número del array numbers en cada iteración.
// Hemos reducido la cantidad de operaciones innecesarias al eliminar la suma manual dentro del bucle y simplemente acumular el resultado en la variable sum.