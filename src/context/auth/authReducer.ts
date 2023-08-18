import { IProfile } from "../../services/auth";
import { authType } from "./types";

const initialState = {
  logged: false,
};

type actionType = {
  type: authType;
  payload: IProfile;
};

export const authReducer = (state = initialState, action: actionType) => {
  switch (action.type) {
    case authType.login:
      return {
        ...state,
        logged: true,
        user: action.payload,
      };

    case authType.logout:
      return {
        logged: false,
      };

    default:
      return state;
  }
};
