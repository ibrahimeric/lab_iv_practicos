/* Implementa una función en JavaScript que maneje una excepción 
cuando se intenta dividir entre cero, mostrando un mensaje de 
error en la página. */

function dividir(dividendo, divisor) {
  try {
        if (divisor === 0) {
            throw new Error("No se puede dividir entre cero.");
        }
        return dividendo / divisor;
    } catch (error) {
        console.error("Error: " + error.message);
        return null;
    }
}

const resultado = dividir(parseFloat(prompt("Ingrese el primer valor: ", "")), parseFloat(prompt("Ingrese el segundo valor: ", "")));

if (resultado !== null) {
    console.log("Resultado de la división:", resultado);
} else {
    console.log("La división no pudo realizarse. No es posible dividir entre '0'");
}