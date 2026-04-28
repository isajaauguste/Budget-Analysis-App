import api from "../lib/axios";

export const getTransactions = (params) => {
  return api.get("/transactions/", { params });
};