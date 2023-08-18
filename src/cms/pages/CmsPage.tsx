import { NavbarComponent } from "../components/Navbar";
import { Outlet } from "react-router-dom";

const CmsPage = () => {
  return (
    <>
      <NavbarComponent />
      <Outlet />
    </>
  );
};

export default CmsPage;
