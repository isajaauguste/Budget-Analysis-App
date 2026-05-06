import { Navigate } from "react-router";
import { useUser } from "./context/useUser";

export default function RequireAdmin({ children }) {
    const { user } = useUser();

    if (!user) return <Navigate to="/login" replace />;
    if (user.role !== "admin") return <Navigate to="/" replace />;

    return children;
}