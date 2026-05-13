import "../styles/Dashboard.css";
import { Link } from "react-router";
import { Wallet, TrendingUp, TrendingDown, Icon } from "lucide-react";
import { useState, useEffect } from "react";
import { getIncome } from "../services/incomeService";
import { getExpense } from "../services/expenseService";
import TransactionsList from "./TransactionsList";
import OverviewChart from "./OverviewChart";

export default function Dashboard() {
  return ""
  //Reikes perkelti i back'a
  
  // const totalIncome = chartData.reduce((sum, item) => sum + item.income, 0);
  // const totalExpense = chartData.reduce((sum, item) => sum + item.expense, 0);
  // const balance = totalIncome - totalExpense;

  // const summary = {
  //   balance,
  //   totalIncome,
  //   totalExpense,
  // };
  // const [chartData, setChartData] = useState([]);
  // const [summary, setSummary] = useState({
  //   balance: 0,
  //   totalIncome: 0,
  //   totalExpense: 0,
  // });

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/v1/dashboard")
      .then((res) => res.json())
      .then((data) => {
        setChartData(data.chartData);
        setSummary(data.summary);
      })
      .catch((err) => console.error(err));
  }, []);

  const formatCurrency = (value) => `€${value}`;
  return (
    <div className="conteiner-style">
      <div className="header-ButtonForAddTransaction">
        <div className="header_style-dashboard">
          <h1 className="header_style-dashboard-h1">Dashboard</h1>
          <p className="header_style-dashboard-p">
            Welcome back! Here's your financial overview.
          </p>
        </div>
        <div>
          <Link className="button_style">Add Transaction</Link>
        </div>
      </div>
      <div className="stats-cards">
        <div className="stats-cards-block">
          <p>Total Balance</p>
          <p>{formatCurrency(summary.balance)}</p>
        </div>
        <div className="stats-cards-block">
          <p>Total Income</p>
          <p>{formatCurrency(summary.totalIncome)}</p>
        </div>
        <div className="stats-cards-block">
          <p>Total Expenses</p>
          <p>{formatCurrency(summary.totalExpense)}</p>
        </div>
      </div>
      <div className="overview-style">
        <OverviewChart />
      </div>
      <div className="recent-transaction-style">
        <div className="title-recent-transaction-block">
          <p>Recent Transaction</p>
          <a href="/transactions" className="link-rencent-trasaction">
            View All →
          </a>
        </div>
        <div className="transaction-list">
          <TransactionsList />
        </div>
      </div>
    </div>
  );
}
