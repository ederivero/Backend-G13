import { conexion } from "../conexion.js";
import { registroUsuarioDto, loginDto } from "../dtos/usuario.dto.js";
import bcrypt from "bcrypt";
import jsonwebtoken from "jsonwebtoken";

export const registroController = async (req, res) => {
  const { error, value } = registroUsuarioDto.validate(req.body);

  if (error) {
    return res.status(400).json({
      message: "error al crear el usuario",
      content: error.details,
    });
  }

  // genera el hash a raiz de la password y el numero de vueltas para generar el salt
  const hashPassword = await bcrypt.hash(value.password, 10);

  const usuarioCreado = await conexion.usuario.create({
    data: {
      ...value,
      password: hashPassword, // remplazamos la contrasena por el hash creado de esa contrasena
    },
  });

  return res.status(201).json({
    message: "usuario creado exitosamente",
    content: usuarioCreado,
  });
};

export const loginController = async (req, res) => {
  const { error, value } = loginDto.validate(req.body);

  if (error) {
    return res.status(400).json({
      message: "Error al hacer el login",
      content: error.details,
    });
  }

  // primero buscar el usuario con ese correo
  const usuarioEncontrado = await conexion.usuario.findUnique({
    where: { email: value.email },
  });

  if (!usuarioEncontrado) {
    return res.status(400).json({
      message: "El usuario no existe en la bd",
    });
  }

  const resultado = await bcrypt.compare(
    value.password,
    usuarioEncontrado.password
  );

  if (resultado === false) {
    return res.status(400).json({
      message: "Contraseña invalida",
    });
  }

  const token = jsonwebtoken.sign(
    {
      sub: usuarioEncontrado.id,
      nombre: usuarioEncontrado.nombre,
    },
    process.env.JWT_SECRET,
    {
      expiresIn: "24h",
    }
  );
  return res.json({
    token,
  });
};
