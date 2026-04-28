import api from "../lib/axios";

export const createExpense = (expenseData) => {
    return api.post("/expense/", expenseData);
};

export const getExpense = () => {
  return api.get("/expense/");
};