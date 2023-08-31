// ECMAscript
import express from "express";

// CommonJs
// const express = require("express");

const productos = [];

const servidor = express();

// antes de cualquier peticion o controlador para que antes de que llegue a ese controlador pase por esta funcionabilidad
servidor.use(express.json());

servidor.get("/", (req, res) => {
  // toda la informacion del cliente estara en el req
  res.json({
    message: "Bienvenido a mi API de Express",
  });
});

servidor
  .route("/productos")
  .post((req, res) => {
    console.log(req.body); // el cuerpo de mi peticion
    const data = req.body;
    productos.push(data);

    res.json({
      message: "Producto creado exitosamente",
    });
  })
  .get((req, res) => {
    res.json({
      content: productos,
    });
  });

servidor.listen(3000, () => {
  console.log("Servidor corriendo exitosamente");
});
