import { useState, useEffect } from "react";
import {
  ResponsiveContainer,
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
} from "recharts";
import "../styles/OverviewChart.css";

function OverviewChart({ data = [] }) {
  
  

  return (
    <div className="chart-container">
      <h2 className="chart-title">Last 7 Days Overview</h2>

      <ResponsiveContainer width="100%" height={300}>
        <AreaChart data={data}>
          <CartesianGrid strokeDasharray="3 3" stroke="#E5E7EB" />

          <XAxis dataKey="date" stroke="#6B7280" />
          <YAxis stroke="#6B7280" />

          <Tooltip contentStyle={tooltipStyle} />

          {/* INCOME */}
          <Area
            type="monotone"
            dataKey="income"
            name="Income"
            stroke="#10B981"
            fill="#10B981"
            fillOpacity={0.5}
            stackId="1"
          />

          {/* EXPENSE */}
          <Area
            type="monotone"
            dataKey="expense"
            name="Expenses"
            stroke="#EF4444"
            fill="#EF4444"
            fillOpacity={0.5}
            stackId="2"
          />
        </AreaChart>
      </ResponsiveContainer>
      <div className="chart-days">
        {(data || []).map((item) => (
          <span key={item.date}>{item.date}</span>
        ))}
      </div>
    </div>
  );
}

const tooltipStyle = {
  backgroundColor: "#fff",
  border: "1px solid #E5E7EB",
  borderRadius: "8px",
  boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
};

export default OverviewChart;
