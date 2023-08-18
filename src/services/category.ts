import axios from "axios";

const request = axios.create({ baseURL: import.meta.env.VITE_BACKEND_URL });

export interface ICategory {
  id: number;
  nombre: string;
  imagen?: string;
  fechaCreacion: string;
}
export const getCategories = async () => {
  return request.get<{ content: ICategory[] }>("/categorias");
};

export const postCategory = async (data: {
  nombre: string;
  imagen?: string;
}) => {
  const token = localStorage.getItem("token");
  if (!token) {
    throw new Error("Se necesita una token");
  }

  return request.post("/categorias", data, {
    headers: { Authorization: `Bearer ${token}` },
  });
};
