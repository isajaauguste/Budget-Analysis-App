import api from "../lib/axios";

export const getExpenseCategories = () => {
  return api.get("/expensecategories/");
};