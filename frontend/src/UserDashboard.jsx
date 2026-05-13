// import { Outlet, Link } from "react-router-dom";
import Sidebar from "./components/Sidebar.jsx";
import Dashboard from "./components/Dashboard.jsx";
import "./styles/AppFullStyle.css";
import Dashboard from "./components/Dashboard.jsx"


function UserDashboard() {
  return (
    <div className="style_pages-dashboard">
      <Sidebar />
      <Dashboard/>
      <h1>hello</h1>
    </div>
  );
}

export default UserDashboard;