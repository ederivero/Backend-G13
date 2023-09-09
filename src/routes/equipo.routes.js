import express from "express";
import { listarEquipos } from "../controllers/equipo.controller.js";

// enrutador de mis rutas de mis controladores de equipos
export const equipoRouter = express.Router();

equipoRouter.get("/equipos", listarEquipos);
