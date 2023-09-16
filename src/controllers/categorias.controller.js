import { CategoriaModel } from '../models/categorias.model.js'
import { crearCategoriaDto } from '../dtos/categorias.dto.js'
import httpError from 'http-errors'

export const crearCategoria = async (req, res) => {
  const { error, value } = crearCategoriaDto.validate(req.body)

  if (error) throw new httpError.BadRequest(error.details)

  const nuevaCategoria = await CategoriaModel.create(value)

  res.status(201).json({
    message: 'Categoria creada exitosamente',
    content: nuevaCategoria.toJSON(), // se usa para retornar solamente la informacion en formato JSON
  })
}

export const devolverCategorias = async (req, res) => {
  const categorias = await CategoriaModel.find()

  res.json({
    content: categorias,
  })
}

export const modificarCategoria = async (req, res) => {
  const { id } = req.params

  const { error, value } = crearCategoriaDto.validate(req.body)

  if (error) throw new httpError.BadRequest(error.details)

  const resultado = await CategoriaModel.updateOne({ _id: id }, value)

  console.log(resultado)

  return res.status(200).json({
    message: 'Categoria actualizada exitosamente',
  })
}
