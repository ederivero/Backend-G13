import express from "express";

const servidor = express();

const PORT = 3000;

servidor.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});
