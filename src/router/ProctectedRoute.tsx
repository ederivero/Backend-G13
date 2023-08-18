import decode from "jwt-decode";
import { useState } from "react";
import { Navigate, Outlet } from "react-router-dom";

export const ProctectedRoute = () => {
  const [token, setToken] = useState(localStorage.getItem("token"));

  if (token) {
    try {
      decode(token);
    } catch (error) {
      setToken(null);
      localStorage.removeItem("token");
    }
  }

  if (!token) {
    return <Navigate to="/login" />;
  }

  return <Outlet />;
};
