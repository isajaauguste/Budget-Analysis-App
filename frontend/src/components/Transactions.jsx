import { useEffect, useState } from "react";
import "../styles/Transactions.css";
import TransactionsList from "./TransactionsList";
import { getTransactions } from "../services/transactionsService";

function Transactions() {
  const [transactions, setTransactions] = useState([]);
  const [filter, setFilter] = useState("all");
  const [sortBy, setSortBy] = useState("date");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);


  const fetchTransactions = async () => {
    try {
      setLoading(true);
      setError(null);

      const res = await getTransactions({
        transaction_type: filter,
        // category_type: filter === "all" ? null : filter,
        sort_by: sortBy,
        limit: 10,
        offset: 0,
      });

      console.log("FILTER:", filter);
      console.log("DATA:", res.data);
      console.log("SENT FILTER:", filter);

      setTransactions(res.data || []);
    } catch (err) {
      console.error(err);
      setError("Failed to load transactions");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchTransactions();
  }, [filter, sortBy]);



  return (
    <>
      <div>
        <div>
          <h2>All Transactions</h2>
          <p>View and manage all your transactions.</p>
        </div>
        <div className="toolbar">
          <div className="filters">
            <button
              className={`tab ${filter === "all" ? "active all" : ""}`}
              onClick={() => setFilter("all")}
            >
              All
            </button>

            <button
              className={`tab ${filter === "income" ? "income" : ""}`}
              onClick={() => setFilter("income")}
            >
              Income
            </button>

            <button
              className={`tab ${filter === "expense" ? "expense" : ""}`}
              onClick={() => setFilter("expense")}
            >
              Expenses
            </button>
          </div>

          <div className="sort">
            <span>Sort by:</span>
            <select value={sortBy} onChange={(e) => setSortBy(e.target.value)}>
              <option value="date">Date</option>
              <option value="amount">Amount</option>
            </select>
          </div>
        </div>
        {loading && <p>Loading...</p>}
        {error && <p>{error}</p>}
        {!loading && (transactions?.length ?? 0) === 0 && <p>No transactions found</p>}
        <div className="transaction_list_style">
          <TransactionsList transactions={transactions} />
        </div>
      </div>
    </>
  );
}
export default Transactions;
