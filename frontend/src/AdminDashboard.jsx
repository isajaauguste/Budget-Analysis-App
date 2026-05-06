import { useUser } from "./context/useUser";


export default function AdminDashboard() {
    const { user } = useUser();

    if (!user || user.role !== "admin") {
        return <h2>Access denied</h2>;
    }

    return (
        <>
            <h2>Admin Dashboard</h2>
        </>
    );
}