import * as S from "./NavbarComponent.style";
import Navbar from "react-bootstrap/Navbar";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import { useNavigate } from "react-router-dom";
import { NavDropdown } from "react-bootstrap";

export const NavbarComponent = () => {
  const navigate = useNavigate();

  return (
    <S.Container
      expand="lg"
      className="bg-body-tertiary"
      bg="dark"
      data-bs-theme="dark"
    >
      <Container>
        <Navbar.Brand
          onClick={() => {
            navigate("/admin");
          }}
          style={{ cursor: "pointer" }}
        >
          Cuchillapp
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <NavDropdown title="Categorias" id="basic-nav-dropdown">
              <NavDropdown.Item
                onClick={() => {
                  navigate("/admin/categories/list");
                }}
              >
                Ver Categorias
              </NavDropdown.Item>
              <NavDropdown.Item
                onClick={() => {
                  navigate("/admin/categories/create");
                }}
              >
                Crear Categoria
              </NavDropdown.Item>
            </NavDropdown>
            <Nav.Link
              onClick={() => {
                navigate("/admin/products");
              }}
            >
              Productos
            </Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </S.Container>
  );
};
