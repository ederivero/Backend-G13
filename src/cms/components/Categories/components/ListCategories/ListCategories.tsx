import { useEffect, useState } from "react";
import { Table } from "react-bootstrap";
import { ICategory, getCategories } from "../../../../../services/category";
import * as S from "./ListCategories.style";

export const ListCategories = () => {
  const [categories, setCategories] = useState<ICategory[]>();

  useEffect(() => {
    const obtenerCategorias = async () => {
      const { data } = await getCategories();

      setCategories(data.content);
    };
    obtenerCategorias();
  }, []);

  return (
    <S.contenedor>
      <Table striped="columns">
        <thead>
          <tr>
            <th>Id</th>
            <th>Nombre</th>
            <th>Imagen</th>
            <th>Fecha Creacion</th>
          </tr>
        </thead>
        <tbody>
          {categories?.map((category, i) => (
            <tr key={i}>
              <td>{category.id}</td>
              <td>{category.nombre}</td>
              <td>
                {category.imagen ? (
                  <img
                    src={`${import.meta.env.VITE_BACKEND_URL}/${
                      category.imagen
                    }`}
                    width="100px"
                  />
                ) : (
                  <b>No hay imagen</b>
                )}
              </td>
              <td>{category.fechaCreacion}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </S.contenedor>
  );
};
