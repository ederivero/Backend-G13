import express from "express";
import {
  registroController,
  loginController,
} from "../controllers/usuario.controller.js";

export const usuarioRouter = express.Router();

usuarioRouter.post("/registro", registroController);
usuarioRouter.post("/login", loginController);
