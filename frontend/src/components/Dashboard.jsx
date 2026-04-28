import "../styles/Dashboard.css";
import { Link } from 'react-router';
import { Wallet, TrendingUp, TrendingDown, Icon } from "lucide-react";
import { useState, useEffect } from "react";
import { getIncome } from "../services/incomeService";
import { getExpense } from "../services/expenseService";
import TransactionsList from "./TransactionsList";
import OverviewChart from "./OverviewChart";

export default function Dashboard(){
    const summary = {
        balance: 1200,
        totalIncome: 3000,
        totalExpense: 1800,
    };

    const formatCurrency = (value) => `€${value}`;
    return(
        <div className="conteiner-style">
            <div className="header-ButtonForAddTransaction">
                <div className="header_style-dashboard">
                    <h1 className="header_style-dashboard-h1">Dashboard</h1>
                    <p className="header_style-dashboard-p">Welcome back! Here's your financial overview.</p>
                </div>
                <div>
                    <Link className="button_style">
                        Add Transaction
                    </Link>
                </div>
            </div>
            <div className="stats-cards">
                <div className="stats-cards-block">
                    <p>Total Balance</p>
                    <p>${0}</p>
                </div>
                <div className="stats-cards-block">
                    <p>Total Income</p>
                    <p>${0}</p>
                </div>
                <div className="stats-cards-block">
                    <p>Total Expenses</p>
                    <p>${0}</p>
                </div>
            </div>
            <div className="overview-style">
                <OverviewChart/>
            </div>
            <div className="recent-transaction-style">
                <div className="title-recent-transaction-block">
                    <p>Recent Transaction</p>
                    <a href="/transactions" className="link-rencent-trasaction">View All →</a>
                </div>
                <div className="transaction-list">
                    <TransactionsList/>
                </div>
            </div>
        </div>
    )
}




