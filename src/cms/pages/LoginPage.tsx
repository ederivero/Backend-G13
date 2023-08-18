import { useContext, useEffect, useState } from "react";
import { Navigate } from "react-router-dom";
import { AuthContext } from "../../context";
import decode from "jwt-decode";
import { Button, Form } from "react-bootstrap";
import { useFormik } from "formik";
import { toast } from "react-hot-toast";

const LoginPage = () => {
  const [token, setToken] = useState(localStorage.getItem("token"));
  const context = useContext(AuthContext);

  useEffect(() => {
    if (token) {
      try {
        decode(token);
      } catch (error) {
        setToken(null);
        localStorage.removeItem("token");
      }
    }
  }, [token]);

  const formik = useFormik({
    initialValues: {
      correo: "",
      password: "",
    },
    onSubmit: async (values, { setSubmitting }) => {
      setSubmitting(true);

      if (!context) {
        throw new Error("Auth Context must be use inside AuthProvide");
      }

      context.login(values);

      toast.success("Bienvenido");

      setSubmitting(false);
    },
    validate: (values) => {
      const errors: { correo?: string; password?: string } = {};

      if (!values.correo) {
        errors.correo = "Este campo es requerido";
      }

      if (!values.password) {
        errors.password = "Este campo es requerido";
      }

      return errors;
    },
  });

  return token ? (
    <Navigate to="/admin" />
  ) : (
    <div
      style={{
        width: "50%",
        margin: "auto",
        padding: "10% 0px",
        border: "20px solid #aeaeae",
        backgroundColor: "#aeaeae",
      }}
    >
      <h1 style={{ textAlign: "center" }}>LOGIN</h1>
      <Form onSubmit={formik.handleSubmit}>
        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Label>Correo</Form.Label>
          <Form.Control
            type="email"
            placeholder="Correo"
            name="correo"
            onChange={formik.handleChange}
            value={formik.values.correo}
          />
          <Form.Text className="text-danger">
            {formik.errors.correo &&
              formik.touched.correo &&
              formik.errors.correo}
          </Form.Text>
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>Password</Form.Label>
          <Form.Control
            type="password"
            placeholder="Password"
            name="password"
            onChange={formik.handleChange}
            value={formik.values.password}
          />
          <Form.Text className="text-danger">
            {formik.errors.password &&
              formik.touched.password &&
              formik.errors.password}
          </Form.Text>
        </Form.Group>

        <Button variant="success" type="submit" disabled={formik.isSubmitting}>
          Iniciar Sesion
        </Button>
      </Form>
    </div>
  );
};

export default LoginPage;
