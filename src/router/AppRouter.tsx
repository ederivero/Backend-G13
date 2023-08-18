import { Routes, Route, Navigate } from "react-router-dom";
import MuestrarioPage from "../muestrario/pages/MuestrarioPage";
import CmsPage from "../cms/pages/CmsPage";
import LoginPage from "../cms/pages/LoginPage";
import { ProctectedRoute } from "./ProctectedRoute";
import { CategoriesComponent } from "../cms/components/Categories";
import { ProductsComponent } from "../cms/components/Products";
import { IndexCmsComponent } from "../cms/components/Index";
import { ListCategories } from "../cms/components/Categories/components/ListCategories/ListCategories";
import { CreateCategory } from "../cms/components/Categories/components/CreateCategory/CreateCategory";

const AppRouter = () => {
  return (
    <>
      <Routes>
        <Route path="/" element={<MuestrarioPage />} />
        <Route element={<ProctectedRoute />}>
          <Route path="/admin" element={<CmsPage />}>
            <Route path="" element={<IndexCmsComponent />} />
            <Route path="categories" element={<CategoriesComponent />}>
              <Route path="" element={<IndexCmsComponent />} />
              <Route path="list" element={<ListCategories />} />
              <Route path="create" element={<CreateCategory />} />
            </Route>
            <Route path="products" element={<ProductsComponent />} />
          </Route>
        </Route>
        <Route path="/login" element={<LoginPage />} />

        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </>
  );
};

export default AppRouter;
