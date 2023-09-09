import { conexion } from "../conexion.js";

export const finalizarPartido = async (req, res) => {
  const { id } = req.params;
  const partidoEncontrado = await conexion.partido.findUnique({
    where: { id: parseInt(id) },
  });
  // tengo que ver si el partido no ha finalizado
  if (partidoEncontrado.finalizado) {
    return res.json({
      message: "El partido ya finalizo!",
    });
  }

  // el partido debe de haber comenzado
  if (partidoEncontrado.empezado === false) {
    return res.json({
      message: "El partido debe empezar para poder finalizarlo",
    });
  }

  await conexion.partido.update({
    data: {
      finalizado: true,
    },
    where: {
      id: partidoEncontrado.id,
    },
  });

  return res.json({
    message: "Partido finalizado exitosamente",
  });
};
