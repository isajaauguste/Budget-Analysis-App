import { useUser } from "./context/useUser";

export default function UserGate({ children }) {
    const { loading } = useUser();
    console.log(loading);
    
    if (loading) return null; 
    return children;
}