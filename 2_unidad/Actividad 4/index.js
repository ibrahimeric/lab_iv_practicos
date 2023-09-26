class Estudiante{
    constructor(nombre, edad, primerParcial, segundoParcial){
        this._nombre = nombre;
        this._edad = edad;
        this._nota_primerParcial = primerParcial;
        this._nota_segundoParcial = segundoParcial;
    }
    promedio(){
        let nota_promedio = (this._nota_primerParcial + this._nota_segundoParcial) / 2;
        console.log(`Datos del estudiante.\nNombre: ${this._nombre}\nEdad: ${this._edad}\nNota del primer parcial: ${this._nota_primerParcial}\nNota del segundo parcial: ${this._nota_segundoParcial}`)
        console.log(`El promedio de las notas del estudiante ${this._nombre} es: ${nota_promedio}\n`)
    }
}

let estudiante1 = new Estudiante("Juan", 20, 7, 9);
let estudiante2 = new Estudiante("Pedro", 21, 6, 7);

estudiante1.promedio();
estudiante2.promedio();