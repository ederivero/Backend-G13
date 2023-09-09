import prisma from "@prisma/client";

// log indica como se va a mostrar las peticiones a la bd
export const conexion = new prisma.PrismaClient({ log: ["query"] });
