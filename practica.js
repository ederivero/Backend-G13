const data = {
  nombre: "eduardo",
  hobbies: { nombre: "volar cometa", experiencia: "mucha" },
  direcciones: [
    {
      calle: "los colones",
      numero: 123,
    },
    {
      calle: "las rosas",
      numero: 456,
    },
  ],
};

// Forma 1
// const nombre = data.nombre;
// console.log(nombre);

// Forma 2
const { nombre } = data;
console.log(nombre);

// Forma 3
const { nombre: nombrecito } = data;
console.log(nombrecito);
