import { Link, useLocation, useNavigate } from "react-router";
import {
  LayoutDashboard,
  ListFilter,
  BarChart3,
  PlusCircle,
  LogOut,
  User,
} from "lucide-react";
import "../styles/Sidebar.css";
import { useUser } from "../context/useUser";

function Sidebar() {
  const location = useLocation();
  const navigate = useNavigate();
  const { user, logout } = useUser();


  const navItems = [
    { path: "/dashboard", label: "Dashboard", icon: LayoutDashboard },
    { path: "/transactions", label: "Transactions", icon: ListFilter },
    { path: "/statistics", label: "Statistics", icon: BarChart3 },
    { path: "/add", label: "Add Transaction", icon: PlusCircle },
  ];
  const handleLogout = async () => {
    await logout();
    navigate("/");
  };
  return (
    <div className="sidebar">
      <div>
        <h1 className="budget-tracker-style">Budget Tracker</h1>
        <p className="manage-your-finances-style">Manage your finances</p>
      </div>
      <nav className="style-nav-bar">
        <ul className="style-nav-icons">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = location.pathname === item.path;

            return (
              <li key={item.path}>
                <Link
                  to={item.path}
                  className={isActive ? "nav-link active" : "nav-link"}
                >
                  <Icon className="iconSize" />
                  <span>{item.label}</span>
                </Link>
              </li>
            );
          })}
        </ul>
      </nav>
      <div className="style-border">
        <div className="style-item">
          <div className="style-flex">
            <User className="userProfile" />
          </div>
          <div>
            <p className="style-username">{user?.username}</p>
            <p className="style-email">{user?.email}</p>
          </div>
        </div>
        <button onClick={handleLogout} className="logout-button-style">
          <LogOut className="LogOut-style" />
          <span>LogOut</span>
        </button>
      </div>
    </div>
  );
}

export default Sidebar;
