import express from "express";
import { finalizarPartido } from "../controllers/partido.controller.js";
import { validarUsuario, validarUsuarioAdmin } from "../utils/validador.js";

export const partidoRouter = express.Router();

partidoRouter.post(
  "/finalizar-partido/:id",
  validarUsuario,
  validarUsuarioAdmin,
  finalizarPartido
);
