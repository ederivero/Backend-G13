import axios from "axios";

const request = axios.create({ baseURL: import.meta.env.VITE_BACKEND_URL });

interface ILogin {
  correo: string;
  password: string;
}

enum TipoUsario {
  ADMIN,
  CLIENTE,
}
export interface IProfile {
  birthday: string;
  correo: string;
  fechaCreacion: string;
  id: number;
  nombre: string;
  tipo: TipoUsario;
}

export const requestLogin = async ({ correo, password }: ILogin) => {
  return request.post<{ content: string }>("/login", {
    correo,
    password,
  });
};

export const requestProfile = async (token: string) => {
  return request.get<{ content: IProfile }>("/perfil", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
};
