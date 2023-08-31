// 1. sin usar la libreria is-odd-num como podriamos saber si un numero es par o impar
let numero = 10;
if (numero % 2 === 0) {
  console.log("Es Par");
} else {
  console.log("Es impar");
}

// 2. se tiene el siguiente arreglo
const notas = [12, 7, 14, 8, 4, 8, 18];
// Filtar solo las notasc que son mayores a 10
let resultado = notas.filter((nota) => {
  return nota > 10;
});

console.log(resultado);

// 3. se tiene el siguiente arreglo
const alumnos = [
  {
    nombre: "edu",
    notas: 18,
  },
  {
    nombre: "juan",
    notas: 10,
  },
  {
    nombre: "mari",
    notas: 11,
  },
  {
    nombre: "yuli",
    notas: 8,
  },
];
// devolver en otro arreglo las notas
// resultado: [18, 10, 11, 8]
resultado = alumnos.map((alumno) => {
  return alumno.notas;
});

console.log(resultado);
