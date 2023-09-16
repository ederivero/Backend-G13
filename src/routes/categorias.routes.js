import Router from 'express'
import * as categoriasController from '../controllers/categorias.controller.js'
import asyncHandler from 'express-async-handler'
export const categoriaRouter = Router()

// si no manejamos el controlador asincrono mediante el asyncHandler si este emite un, entoncess no podra ser manejado por el errorHandler de nuestro proyecto
categoriaRouter
  .route('/categorias')
  .post(asyncHandler(categoriasController.crearCategoria))
  .get(asyncHandler(categoriasController.devolverCategorias))

categoriaRouter.route('/categoria/:id').put(asyncHandler(categoriasController.modificarCategoria))
