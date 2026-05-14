// import { Outlet, Link } from "react-router-dom";
import Sidebar from "./components/Sidebar.jsx";
import Dashboard from "./components/Dashboard.jsx";
import "./styles/AppFullStyle.css";


function UserDashboard() {
  return (
    <div className="style_pages-dashboard">
      <Sidebar />
      <Dashboard/>
    </div>
  );
}

export default UserDashboard;