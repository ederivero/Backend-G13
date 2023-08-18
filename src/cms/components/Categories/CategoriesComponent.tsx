import * as S from "./CategoriesComponent.style";
import { Outlet } from "react-router-dom";

export const CategoriesComponent = () => {
  return (
    <S.Container>
      <Outlet />;
    </S.Container>
  );
};
