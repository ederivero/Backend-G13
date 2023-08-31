import sumar from "./funcionabilidad.js";
// cuando si se le coloca llaves (destructuracion) se estara utilizando las funciones, clases, etc que no son por default
import { restar } from "./funcionabilidad.js";
// cuando a la importacion no se coloca llaves se esta importando la funcion, clase, etc, por default
import isOdd from "is-odd-num";

const nombre = "eduardo";

let edad = 20;

edad = 18;

console.log(edad);

let resultado = sumar(5, 4);

console.log(resultado);

resultado = isOdd(10);

console.log(resultado);
