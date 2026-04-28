import api from "../lib/axios";

export const createIncome = (incomeData) => {
    return api.post("/income/", incomeData);
};

export const getIncome = () => {
  return api.get("/income/");
};