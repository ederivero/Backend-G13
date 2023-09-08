/*
  Warnings:

  - A unique constraint covering the columns `[nombre]` on the table `jornadas` will be added. If there are existing duplicate values, this will fail.

*/
-- CreateIndex
CREATE UNIQUE INDEX "jornadas_nombre_key" ON "jornadas"("nombre");
