import Joi from 'joi'

export const crearCategoriaDto = Joi.object({
  nombre: Joi.string().required(),
  habilitado: Joi.boolean().optional(),
})
