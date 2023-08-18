import { IProfile } from "../../services/auth";

export enum authType {
  login,
  logout,
}

export interface AuthContextType {
  login: ({ correo, password }: { correo: string; password: string }) => void;
  state: {
    logged: boolean;
    user?: IProfile;
  };
}
