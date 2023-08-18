import axios from "axios";

const request = axios.create({ baseURL: import.meta.env.VITE_BACKEND_URL });

interface IPutImage {
  message: string;
  content: {
    imagen: string;
  };
}

export const putImage = async (data: FormData) => {
  const token = localStorage.getItem("token");
  if (!token) {
    throw new Error("Se necesita una token");
  }

  return request.post<IPutImage>("/subir-imagen", data, {
    headers: {
      "Content-Type": "multipart/form-data",
      Authorization: `Bearer ${token}`,
    },
  });
};
