import express from 'express'
import mongoose from 'mongoose'
import dotenv from 'dotenv'
import { categoriaRouter } from './routes/categorias.routes.js'
// desde node v20.6.0 no es necesario el uso de esta libreria https://nodejs.org/en/blog/release/v20.6.0
// sirve para leer las variables declaradas en el archivo .env y las configura como variables de entorno
dotenv.config()

const server = express()
const PORT = process.env.PORT ?? 3000

const conectarBd = async () => {
  await mongoose.connect(process.env.MONGODB_URL)
  console.log('Conexion exitosa a la base de datos')
}

// Creamos un manejador de errores
// se va a comportar como un middleware
function errorHandler(error, req, res, next) {
  console.log(error)
  console.log('------')
  console.log(error.status)
  console.log('------')
  console.log(error.message)

  return res.json({
    message: 'Error!',
  })
}

// aca utilizaremos el manejador de errores
// ESTE MANEJADOR SIEMPRE DEBE IR DESPUES DE TODAS LAS RUTAS!!!
server.use(errorHandler)

// aca recien van nuestras rutas, luego del errorHandler
server.use(categoriaRouter)

server.listen(PORT, async () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`)
  await conectarBd()
})
