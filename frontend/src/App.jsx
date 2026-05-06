import { Routes, Route } from "react-router-dom";
import "./styles/AppFullStyle.css";
import Login from "./Login.jsx";
import Register from "./Register.jsx";
import UserDashboard from "./Userdashboard.jsx";
import AdminDashboard from "./AdminDashboard.jsx";
import RequireAdmin from "./RequireAdmin.jsx";
import RequireUser from "./RequireUser.jsx";
// import { Routes, Route } from "react-router";

function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route
          path="/admin"
          element={
            <RequireAdmin>
              <AdminDashboard />
            </RequireAdmin>
          }
        />
        <Route
          path="/dashboard"
          element={
            <RequireUser>
              <UserDashboard />
            </RequireUser>
          }
        />
      </Routes>
    </>
  );
}

export default App;
