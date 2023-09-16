import Router from 'express'
import * as categoriasController from '../controllers/categorias.controller.js'

export const categoriaRouter = Router()

categoriaRouter.route('/categorias').post(categoriasController.crearCategoria)
