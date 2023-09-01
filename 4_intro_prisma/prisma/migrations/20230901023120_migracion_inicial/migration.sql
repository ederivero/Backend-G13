-- CreateEnum
CREATE TYPE "NivelAcademico" AS ENUM ('PRIMARIA', 'SECUNDARIA');

-- CreateEnum
CREATE TYPE "TipoGrupoSanguineo" AS ENUM ('A_POSITIVO', 'A_NEGATIVO', 'B_POSITIVO', 'B_NEGATIVO', 'AB_POSITIVO', 'AB_NEGATIVO', 'O_POSITIVO', 'O_NEGATIVO');

-- CreateTable
CREATE TABLE "alumnos" (
    "id" UUID NOT NULL,
    "nombre" TEXT NOT NULL,
    "apellido" TEXT NOT NULL,
    "correo" TEXT NOT NULL,
    "telefono_emergencia" TEXT NOT NULL,
    "grupoSanguineo" "TipoGrupoSanguineo",

    CONSTRAINT "alumnos_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "grados" (
    "id" UUID NOT NULL,
    "nombre_numerico" TEXT NOT NULL,
    "nombre_texto" TEXT NOT NULL,

    CONSTRAINT "grados_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "secciones" (
    "id" UUID NOT NULL,
    "nombre" TEXT NOT NULL,

    CONSTRAINT "secciones_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "anio_lectivos" (
    "id" UUID NOT NULL,
    "anio" TEXT NOT NULL,
    "nivel" "NivelAcademico" NOT NULL DEFAULT 'PRIMARIA',
    "alumno_id" UUID NOT NULL,
    "grado_id" UUID NOT NULL,
    "seccion_id" UUID NOT NULL,

    CONSTRAINT "anio_lectivos_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "alumnos_correo_key" ON "alumnos"("correo");

-- CreateIndex
CREATE UNIQUE INDEX "secciones_nombre_key" ON "secciones"("nombre");

-- AddForeignKey
ALTER TABLE "anio_lectivos" ADD CONSTRAINT "anio_lectivos_alumno_id_fkey" FOREIGN KEY ("alumno_id") REFERENCES "alumnos"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "anio_lectivos" ADD CONSTRAINT "anio_lectivos_grado_id_fkey" FOREIGN KEY ("grado_id") REFERENCES "grados"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "anio_lectivos" ADD CONSTRAINT "anio_lectivos_seccion_id_fkey" FOREIGN KEY ("seccion_id") REFERENCES "secciones"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
