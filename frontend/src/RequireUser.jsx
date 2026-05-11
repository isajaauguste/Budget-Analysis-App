import { Navigate } from "react-router";
import { useUser } from "./context/useUser";

export default function RequireAuth({ children }) {
    const { user } = useUser();
    if (!user) return <Navigate to="/" replace />;
    return children;
}