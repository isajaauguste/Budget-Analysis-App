import { FaArrowUp, FaArrowDown, FaEdit, FaTrash } from "react-icons/fa";
import "../styles/TransactionsList.css";

function TransactionsList({ transactions = []}) {
  
  return (
    <div className="transactions-container">
      {transactions.map((t) => (
        <div key={t.id} className={`transaction-card ${t.category_type}`}>
          <div className="icon">
            {t.category_type === "income" ? (
              <FaArrowUp />
            ) : (
              <FaArrowDown />
            )}
          </div>

          <div className="details">
            <div className="description">{t.name}</div>
            <div className="category-date">
              {t.category || t.category_id || "Category"} &nbsp;&middot;&nbsp;{" "}
              {t.date ? new Date(t.date).toLocaleDateString() : ""}
            </div>
          </div>
            {/*pridetas t.category_type*/}
          <div className={`amount ${t.category_type === "income" ? "positive" : "negative"}`}>
            {t.category_type === "income" ? "+" : "-"}€{t.amount.toFixed(2)}
          </div>

          <div className="actions">
            <FaEdit className="action-icon" />
            <FaTrash className="action-icon" />
          </div>
        </div>
      ))}
    </div>
  );
}

export default TransactionsList;