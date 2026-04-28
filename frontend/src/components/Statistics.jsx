import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer,
} from "recharts";
import "../styles/Statistics.css";
function Statistics() {
  return (
    <>
      <div>
        <div>
          <p>Statistics & Analytics</p>
          <p>Detailed insights into your financial patterns.</p>
        </div>
        <div className="choice_style-statistics">
          <ul className="category_statistics">
            <li>
              <a href="">Las 7 Days</a>
            </li>
            <li>
              <a href="">Last Month</a>
            </li>
            <li>
              <a href="">Last Year</a>
            </li>
          </ul>
        </div>
        <div className="pie_chart-style">
          <div className="pie_chart-edit">
            <p>Expenses by Category</p>
          </div>
          <div className="pie_chart-edit">
            <p>Income by Category</p>
          </div>
        </div>
      </div>
    </>
  );
}
export default Statistics;
