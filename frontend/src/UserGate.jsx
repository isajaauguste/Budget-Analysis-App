import { useUser } from "./context/useUser";

export default function UserGate({ children }) {
    const { loading } = useUser();
    if (loading) return null; 
    return children;
}