import prisma from "@prisma/client";

const conexion = new prisma.PrismaClient();

async function poblarBD() {
  const equipos = [
    {
      nombre: "Argentina",
    },
    {
      nombre: "Bolivia",
    },
    {
      nombre: "Brazil",
    },
    {
      nombre: "Chile",
    },
    {
      nombre: "Colombia",
    },
    {
      nombre: "Ecuador",
    },
    {
      nombre: "Paraguay",
    },
    {
      nombre: "Peru",
    },
    {
      nombre: "Uruguay",
    },
    {
      nombre: "Venezuela",
    },
  ];

  const jornadas = [
    {
      nombre: "Jornada 1",
      fechaInicial: new Date("2023-09-07"),
      fechaFinal: new Date("2023-09-08"),
    },
    {
      nombre: "Jornada 2",
      fechaInicial: new Date("2023-09-09"),
      fechaFinal: new Date("2023-09-09"),
    },
    {
      nombre: "Jornada 3",
      fechaInicial: new Date("2023-10-12"),
      fechaFinal: new Date("2023-10-12"),
    },
    {
      nombre: "Jornada 4",
      fechaInicial: new Date("2023-10-17"),
      fechaFinal: new Date("2023-10-17"),
    },
    {
      nombre: "Jornada 5",
      fechaInicial: new Date("2023-12-25"),
      fechaFinal: new Date("2023-12-25"),
    },
    {
      nombre: "Jornada 6",
      fechaInicial: new Date("2023-12-25"),
      fechaFinal: new Date("2023-12-25"),
    },
    {
      nombre: "Jornada 7",
      fechaInicial: new Date("2023-12-25"),
      fechaFinal: new Date("2023-12-25"),
    },
    {
      nombre: "Jornada 8",
      fechaInicial: new Date("2023-12-25"),
      fechaFinal: new Date("2023-12-25"),
    },
    {
      nombre: "Jornada 9",
      fechaInicial: new Date("2023-12-25"),
      fechaFinal: new Date("2023-12-25"),
    },
    {
      nombre: "Jornada 10",
      fechaInicial: new Date("2023-12-25"),
      fechaFinal: new Date("2023-12-25"),
    },
    {
      nombre: "Jornada 11",
      fechaInicial: new Date("2023-12-25"),
      fechaFinal: new Date("2023-12-25"),
    },
    {
      nombre: "Jornada 12",
      fechaInicial: new Date("2023-12-25"),
      fechaFinal: new Date("2023-12-25"),
    },
    {
      nombre: "Jornada 13",
      fechaInicial: new Date("2023-12-25"),
      fechaFinal: new Date("2023-12-25"),
    },
    {
      nombre: "Jornada 14",
      fechaInicial: new Date("2023-12-25"),
      fechaFinal: new Date("2023-12-25"),
    },
    {
      nombre: "Jornada 15",
      fechaInicial: new Date("2023-12-25"),
      fechaFinal: new Date("2023-12-25"),
    },
    {
      nombre: "Jornada 16",
      fechaInicial: new Date("2023-12-25"),
      fechaFinal: new Date("2023-12-25"),
    },
    {
      nombre: "Jornada 17",
      fechaInicial: new Date("2023-12-25"),
      fechaFinal: new Date("2023-12-25"),
    },
    {
      nombre: "Jornada 18",
      fechaInicial: new Date("2023-12-25"),
      fechaFinal: new Date("2023-12-25"),
    },
  ];

  for (let index = 0; index < equipos.length; index++) {
    const equipo = equipos[index];

    await conexion.equipo.upsert({
      create: equipo,
      update: {},
      where: { nombre: equipo.nombre },
    });
  }

  for (let index = 0; index < jornadas.length; index++) {
    const jornada = jornadas[index];

    // upsert > si existe el registro, procedera con la actualizacion, caso contrario realizara la creacion
    await conexion.jornada.upsert({
      create: jornada,
      update: {},
      where: {
        nombre: jornada.nombre,
      },
    });
  }

  console.log("Comando ejecutado con exito");
}

poblarBD();
