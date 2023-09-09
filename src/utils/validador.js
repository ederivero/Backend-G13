import jsonwebtoken from "jsonwebtoken";
import { conexion } from "../conexion.js";
import { TipoUsuario } from "@prisma/client";

// middleware > intermediario entre la peticion y el request final sirve para ver el request antes de que llegue al controlador final y por ende este puede interrumpir el flujo o cancelarlo
export const validarUsuario = async (req, res, next) => {
  const { authorization } = req.headers;

  if (!authorization) {
    return res.status(403).json({
      message: "Se necesita una token para esta peticion",
    });
  }

  const token = authorization.split(" ")[1];

  if (!token) {
    return res.status(403).json({
      message: "El formato para enviar la token es <Bearer YOUR_TOKEN>",
    });
  }
  // si logra decodificar la token devolvera el payload, caso contrario lanzara un error
  try {
    const payload = jsonwebtoken.verify(token, process.env.JWT_SECRET);

    const usuarioEncontrado = await conexion.usuario.findUniqueOrThrow({
      where: { id: payload.sub },
    });

    req.user = usuarioEncontrado;

    console.log(payload);
  } catch (error) {
    return res.status(403).json({
      message: "Error al validar el usuario",
      content: error.message,
    });
  }
  // es la funcion que le indicara al middleware que puede pasar al siguiente middleware o controlador final
  next();
};

export const validarUsuarioAdmin = async (req, res, next) => {
  console.log(req.user);
  //req.user > usuario validado previamente
  if (req.user.tipoUsuario === TipoUsuario.ADMIN) {
    next();
  } else {
    return res.status(403).json({
      message: "No tienes los permisos suficientes para realizar esta accion",
    });
  }
};
