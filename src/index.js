import express from "express";
import cors from "cors";
import { equipoRouter } from "./routes/equipo.routes.js";
import { usuarioRouter } from "./routes/usuario.routes.js";

const servidor = express();
servidor.use(express.json());
servidor.use(cors()); // cualquier dominio a cualquier metodo y con cualquier header va a poder consultar nuestra API

servidor.use(equipoRouter);
servidor.use(usuarioRouter);

// para utilizar las variables de entorno en node se hace mediante el modulo process.env
// si la parte de la izq es null o undefined entonces tomara la parte de la derecha
// si no lo es, tomara la de la izq
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing
const PORT = process.env.PORT ?? 3000; // nullish coale`scing operator (Operadora de fusión nula)

// operador logico AND
// primero validara que la condicion de la izq sea verdadero (o no sea nulo o indefinido)
// y procedera con lo de la derecha, si es falso el valor de la izq entonces retornara false
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND
// process.env.PORT && 3000;

// operador logico OR
// si el valor de la izq es falso o null o undefined tomara el de la derecha, caso contrarion tomara el de la izq
// la diferencia con el '??' es que a parte de valir si es null o undefined tambien validara si es false osea que si le pasamos el valor de 0 este se considera false en js y por ende tomara el valor de la derecha
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR
// process.env.PORT || 3000;

servidor.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});
