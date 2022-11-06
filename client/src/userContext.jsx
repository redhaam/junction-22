import { createContext, useContext, useReducer, useEffect } from "react";

import { fetchClient } from "./fetch";

const UserContext = createContext();

const initialState = {
  status: "idle",
  user: null,
  error: null,
};

function authReducer(auth, action) {
  switch (action.type) {
    case "logout":
      localStorage.removeItem("token");
      return initialState;
    case "login":
      return { ...auth, status: "pending" };
    case "success":
      return { status: "success", user: action.user, error: null };
    case "reject":
      return { ...auth, status: "rejected", error: action.error };
    default:
      throw new Error(`Unhandled action type: ${action.type}`);
  }
}

function UserProvider({ children }) {
  const [auth, dispatch] = useReducer(authReducer, initialState);

  async function doLogin() {
    try {
      dispatch({ type: "login" });

      const res = await fetchClient("auth/me");
      dispatch({
        type: "success",
        user: res,
      });
    } catch (error) {
      dispatch({ type: "reject", error });
    }
  }

  function doLogout() {
    dispatch({ type: "logout" });
  }

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      doLogin();
    } else dispatch({ type: "reject" });
  }, []);

  return (
    <UserContext.Provider
      value={{
        connected: auth.status == "success",
        ...auth,
        doLogin,
        doLogout,
      }}>
      {children}
    </UserContext.Provider>
  );
}

const useAuth = () => useContext(UserContext);

export { UserProvider, useAuth };
