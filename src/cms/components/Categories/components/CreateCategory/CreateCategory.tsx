import { Form, Button } from "react-bootstrap";
import * as S from "./CreateCategory.style";
import { putImage } from "../../../../../services/images";
import { useState } from "react";
import { useFormik } from "formik";
import { postCategory } from "../../../../../services/category";
import toast from "react-hot-toast";

export const CreateCategory = () => {
  const [imagen, setImagen] = useState<string>();

  const manejoImagen = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const formData = new FormData();

    if (e.currentTarget.files) {
      formData.append("imagen", e.currentTarget.files![0]);

      const { data } = await putImage(formData);
      setImagen(data.content.imagen);
    }
  };

  const formik = useFormik({
    initialValues: {
      nombre: "",
    },
    onSubmit: async (values, { setSubmitting }) => {
      setSubmitting(true);

      await postCategory({ nombre: values.nombre, imagen: imagen });
      toast.success("Categoria creada exitosamente");

      setSubmitting(false);
    },
    validate: (values) => {
      const errors: { nombre?: string } = {};

      if (!values.nombre) {
        errors.nombre = "Este campo es requerido";
      }

      return errors;
    },
  });

  return (
    <S.contenedor>
      <Form onSubmit={formik.handleSubmit}>
        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Label>Nombre</Form.Label>
          <Form.Control
            type="text"
            name="nombre"
            placeholder="Ingresa el nombre de la categoria"
            value={formik.values.nombre}
            onChange={formik.handleChange}
          />
          <Form.Text className="text-danger">
            {formik.errors.nombre &&
              formik.touched.nombre &&
              formik.errors.nombre}
          </Form.Text>
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>Imagen</Form.Label>
          <Form.Control
            type="file"
            accept="image/png, image/gif, image/jpeg"
            name="imagen"
            onChange={manejoImagen}
          />
        </Form.Group>

        <Button
          variant="success"
          type="submit"
          disabled={formik.isSubmitting}
          style={{ width: "100%" }}
        >
          Crear
        </Button>
      </Form>
    </S.contenedor>
  );
};
