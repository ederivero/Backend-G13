import express from "express";
import Prisma, { TipoGrupoSanguineo } from "@prisma/client";
import Joi from "joi";
import swaggerUI from "swagger-ui-express";
import archivoSwagger from "./swagger.json";

const conexion = new Prisma.PrismaClient();

const servidor = express();

const seccionSchema = Joi.object({
  nombre: Joi.string().required(),
});

const alumnoSchema = Joi.object({
  nombre: Joi.string().required(),
  apellido: Joi.string().required(),
  correo: Joi.string().email().required(),
  // Sirve para que solo acepte numeros siendo un string
  telefonoEmergencia: Joi.string().pattern(new RegExp("^[0 - 9]")).required(),
  grupoSanguineo: Joi.string()
    .valid(
      TipoGrupoSanguineo.AB_NEGATIVO,
      TipoGrupoSanguineo.AB_POSITIVO,
      TipoGrupoSanguineo.A_NEGATIVO,
      TipoGrupoSanguineo.A_POSITIVO,
      TipoGrupoSanguineo.B_NEGATIVO,
      TipoGrupoSanguineo.B_POSITIVO,
      TipoGrupoSanguineo.O_NEGATIVO,
      TipoGrupoSanguineo.O_POSITIVO
    )
    .optional(),
});

servidor.use(express.json());

const PORT = 3000;

servidor
  .route("/grados")
  .post(async (req, res) => {
    const { body: data } = req;

    try {
      const resultado = await conexion.grado.create({
        data,
        //  {
        //   nombreNumerico: body.nombreNumerico,
        //   nombreTexto: body.nombreTexto,
        // },
      });
      console.log(resultado);
      res.json({
        message: "Grado creado exitosamente",
      });
    } catch (error) {
      res.json({
        message: "Error al crear el grado",
      });
    }
  })
  .get(async (req, res) => {
    const resultado = await conexion.grado.findMany();

    res.json({
      content: resultado,
    });
  });

servidor
  .route("/grado/:id")
  .all(async (req, res, next) => {
    // se viene a comportar como un intermediario (MIDDLEWARE)
    const { id } = req.params;
    try {
      const gradoEncontrado = await conexion.grado.findUniqueOrThrow({
        where: { id: id },
      });

      req.grado = gradoEncontrado;
    } catch (error) {
      if (error instanceof Prisma.Prisma.PrismaClientKnownRequestError) {
        // Error para cualquier consulta erronea a la base de datos
        return res.status(400).json({
          message: "Id del grado invalido",
        });
      }

      return res.status(400).json({
        message: "Error al buscar el grado",
      });
    }

    next();
  })
  .get(async (req, res) => {
    console.log(req.grado);

    return res.json({
      content: req.grado,
    });
  })
  .put(async (req, res) => {
    const { body } = req;

    const respuesta = await conexion.grado.update({
      where: { id: req.grado.id },
      data: body,
    });

    return res.json({
      message: "Grado actualizado exitosamente",
      content: respuesta,
    });
  })
  .delete(async (req, res) => {
    const respuesta = await conexion.grado.delete({
      where: { id: req.grado.id },
    });

    return res.json({
      message: "Grado eliminado exitosamente",
      content: respuesta,
    });
  });

servidor
  .route("/secciones")
  .post(async (req, res) => {
    const { body } = req;

    // value > la informacion correctamente validada
    // error > los errores
    // Si hay error no hay value y si hay value no hay error
    const { value, error } = seccionSchema.validate(body);

    if (error) {
      return res.status(400).json({
        message: "Error al crear la seccion",
        content: error.details,
      });
    }

    const seccionCreada = await conexion.seccion.create({ data: value });

    return res.json({
      message: "Seccion creada exitosamente",
      content: seccionCreada,
    });
  })
  .get(async (req, res) => {
    const resultado = await conexion.seccion.findMany();

    return res.json({
      content: resultado,
    });
  });

servidor.route("/alumnos").post(async (req, res) => {
  const { error, value } = alumnoSchema.validate(req.body);

  if (error) {
    return res.json({
      message: "Error al crear el alumno",
      content: error.details,
    });
  }

  const respuesta = await conexion.alumno.create({ data: value });

  return res.status(201).json({
    message: "Alumno creado exitosamente",
    content: respuesta,
  });
});
servidor.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});
