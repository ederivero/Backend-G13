import { CategoriaModel } from '../models/categorias.model.js'
import { crearCategoriaDto } from '../dtos/categorias.dto.js'
import HttpErrors from 'http-errors'

export const crearCategoria = async (req, res) => {
  const { error, value } = crearCategoriaDto.validate(req.body)

  if (error) throw new HttpErrors.BadRequest('Error al crear la categoria')

  const nuevaCategoria = await CategoriaModel.create(value)

  res.status(201).json({
    message: 'Categoria creada exitosamente',
    content: nuevaCategoria.toJSON(), // se usa para retornar solamente la informacion en formato JSON
  })
}
