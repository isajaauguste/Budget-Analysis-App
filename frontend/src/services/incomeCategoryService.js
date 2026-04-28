import api from "../lib/axios";

export const getIncomeCategories = () => {
  return api.get("/incomecategories/");
};