import { ReactNode, useReducer, useEffect, useMemo } from "react";
import { AuthContext } from "./AuthContext";
import { authReducer } from "./authReducer";
import { authType } from "./types";
import { IProfile, requestLogin, requestProfile } from "../../services/auth";
import decode from "jwt-decode";
import { useNavigate } from "react-router-dom";

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const navigate = useNavigate();
  const initialState: { logged: boolean; user?: IProfile | null } = useMemo(
    () => ({
      logged: false,
    }),
    []
  );

  const [state, dispatch] = useReducer(authReducer, initialState);

  useEffect(() => {
    const token = localStorage.getItem("token");
    const usuario = localStorage.getItem("usuario");
    if (token && usuario) {
      const { exp } = decode<{ exp: number }>(token);

      if (new Date(exp * 1000) < new Date()) {
        localStorage.removeItem("token");
        localStorage.removeItem("usuario");
      }

      initialState.user = JSON.parse(usuario);
      initialState.logged = true;
    } else {
      initialState.logged = false;
    }
  }, [initialState]);

  const login = async ({
    correo,
    password,
  }: {
    correo: string;
    password: string;
  }) => {
    const localToken = localStorage.getItem("token");

    if (localToken) {
      const {
        data: { content: user },
      } = await requestProfile(localToken);

      localStorage.setItem("usuario", JSON.stringify(user));
    } else {
      const {
        data: { content: token },
      } = await requestLogin({ correo, password });

      const payload = decode<{ sub: number }>(token);
      console.log(payload);

      localStorage.setItem("token", token);

      const {
        data: { content: user },
      } = await requestProfile(token);

      localStorage.setItem("usuario", JSON.stringify(user));
      navigate("/admin");
    }

    const action = {
      type: authType.login,
      payload: JSON.parse(
        localStorage.getItem("usuario") as string
      ) as IProfile,
    };

    dispatch(action);
  };
  return (
    <AuthContext.Provider value={{ login, state }}>
      {children}
    </AuthContext.Provider>
  );
};
