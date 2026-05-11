import { useEffect, useState } from "react";
import api from "../lib/axios";
import { UserContext } from "./UserContext";
import { data } from "react-router";

export const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  const login = async (data) => {
    const res = await api.post("/auth/login", data);
    
    setUser(res.data);
    setLoading(false);
    return res.data;
  };

  const logout = async () => {
    await api.post("/auth/logout");
    setUser(null);
  };

  // useEffect(() => {
  //   const loadUser = async () => {
  //     const res = await api.get("/users/me");
  //     console.log(res.data);
  //     setUser(res.data);
  //     setLoading(false);
  //   };

  //   loadUser();
  // }, []);

  useEffect(() => {
    const loadUser = async () => {
      try {
        const res = await api.get("/users/me");
        setUser(res.data.data);
      } catch {
        setUser(null);
      } finally {
        setLoading(false);
      }
    };

  loadUser();
  }, []);
  
  return (
    <UserContext.Provider value={{ user, login, logout, loading }}>
      {children}
    </UserContext.Provider>
  );
};
