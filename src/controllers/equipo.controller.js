import { conexion } from "../conexion.js";

export const listarEquipos = async (req, res) => {
  const resultado = await conexion.equipo.findMany();

  return res.json({
    content: resultado,
  });
};
