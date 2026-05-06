import { useEffect, useState } from "react";
import api from "../lib/axios";
import { UserContext } from "./UserContext";

export const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  const login = async (data) => {
    const res = await api.post("/user/login", data);
    setUser(res.data.data);
    setLoading(false);
    return res.data.data;
  };

  const logout = async () => {
    await api.post("/user/logout");
    setUser(null);
  };

  // useEffect(() => {
  //   const loadUser = async () => {
  //     const res = await api.get("/user/me");
  //     setUser(res.data.data);
  //     setLoading(false);
  //   };

  //   loadUser();
  // }, []);

  return (
    <UserContext.Provider value={{ user, login, logout, loading }}>
      {children}
    </UserContext.Provider>
  );
};
