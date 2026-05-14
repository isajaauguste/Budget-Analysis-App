import { Routes, Route } from "react-router";
import "./styles/AppFullStyle.css";

import Login from "./Login.jsx";
import Register from "./Register.jsx";

import UserDashboard from "./UserDashboard.jsx";
import AdminDashboard from "./AdminDashboard.jsx";

import RequireAdmin from "./RequireAdmin.jsx";
import RequireUser from "./RequireUser.jsx";
import Transactions from "./components/Transactions.jsx";

// import Dashboard from "./components/Dashboard.jsx";
// import Transactions from "./components/Transactions.jsx";
// import Statistics from "./components/Statistics.jsx";
// import TransactionForm from "./components/TransactionForm.jsx";

function App() {
  return (
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
      <Route 
      path="/transactions"
      element={
        <RequireUser>
          <Transactions/>
        </RequireUser>
      }
      />
    </Routes>
  );
}

export default App;
