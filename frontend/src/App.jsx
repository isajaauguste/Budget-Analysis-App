import { BrowserRouter, Routes, Route } from "react-router-dom";
import TransactionForm from "./components/TransactionForm";
import TransactionsList from "./components/TransactionsList";
import Sidebar from "./components/Sidebar";
import Dashboard from "./components/Dashboard";
import Transactions from "./components/Transactions";
import Statistics from "./components/Statistics";
import "./styles/AppFullStyle.css";
// import { Routes, Route } from "react-router";

function App() {
  return (
    <>
        <div className="style_pages-dashboard">
          <Sidebar />

          <div style={{ flex: 1 }}>
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/transactions" element={<Transactions />} />
              <Route path="/statistics" element={<Statistics />} />
              <Route path="/add" element={<TransactionForm />} />
            </Routes>
          </div>
        </div>
    </>
  );
}

export default App;
