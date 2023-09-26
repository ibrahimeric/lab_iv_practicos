/* Escribe una función en JavaScript que verifique si un 
número ingresado por el usuario es primo. Si no es primo, lanza 
una excepción con un mensaje correspondiente. */

function esPrimo(numero) {
    if (numero <= 1) {
        return false;
    }
  
    if (numero === 2) {
        return true;
    }
  
    if (numero % 2 === 0) {
        return false;
    }
  
    for (let i = 3; i <= Math.sqrt(numero); i += 2) {
        if (numero % i === 0) {
            return false;
        }
    }
  
    return true;
}

const numero = parseFloat(prompt("Introduce un numero para verificar si es primo:", ""));
if (esPrimo(numero)) {
    console.log(`El numero ${numero} es primo.`);
} else {
    console.log(`El numero ${numero} no es primo.`);
}
