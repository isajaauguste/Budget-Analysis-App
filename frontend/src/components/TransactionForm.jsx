import { useEffect, useState } from "react";
import { useForm } from "react-hook-form";
import { createIncome } from "../services/incomeService";
import { getIncomeCategories } from "../services/incomeCategoryService";
import { createExpense } from "../services/expenseService";
import { getExpenseCategories } from "../services/expenseCategoryService";
import '../styles/TransactionForm.css';



function TransactionForm() {
    const {
        register,
        handleSubmit,
        formState: { errors },
        reset,
        setValue,
        watch,
    } = useForm({
        defaultValues: {
            type: 'expense',
            amount: "",
            name: "",
            // date: new Date().toISOString().split("T")[0],
            category_id: "",
        },
    });

    const selectedType = watch('type');


    const [categories, setCategories] = useState([]);
    const [serverError, setServerError] = useState("");
    const [successMessage, setSuccessMessage] = useState("");


    useEffect(() => {
        const fetchCategories = async () => {
            try {
                let res;

                if (selectedType === "income") {
                    res = await getIncomeCategories();
                } else if (selectedType === "expense") {
                    res = await getExpenseCategories();
                }

                setCategories(res.data);
                setValue("category_id", "");
            } catch (error) {
                console.error(error);
                setServerError("Failed to load categories");
            }
        };

        fetchCategories();
    }, [selectedType]);


    const onSubmit = async (data) => {
        try {
            setServerError("");
            setSuccessMessage("");

            const payload = {
                amount: Number(data.amount),
                name: data.name,
                date: data.date,
                category_id: Number(data.category_id),
            };

            if (data.type === "income") {
                await createIncome(payload);
            } else {
                await createExpense(payload);
            }

            setSuccessMessage("Transaction added successfully");
            reset();
        } catch (error) {
            console.error(error);
            setServerError("Failed to add transaction");
        }
    };


    return (
        <div className="transaction-form-container">

            <form onSubmit={handleSubmit(onSubmit)}>
                <div className="form-group">
                    <label>Transaction Type</label>
                    <div className="type-toggle">
                        <button
                            type="button" className={selectedType === "expense" ? "active expense" : ""}
                            onClick={() => setValue("type", "expense")}
                        >
                            Expense
                        </button>

                        <button
                            type="button" className={selectedType === "income" ? "active income" : ""}
                            onClick={() => setValue("type", "income")}
                        >
                            Income
                        </button>
                    </div>
                </div>



                <div className="form-group">
                    <label htmlFor="amount">Amount</label>
                    <div className="amount-input-wrapper">
                        <span className="currency-symbol">€</span>
                        <input
                            type="number"
                            {...register("amount", {
                                required: "Amount is required",
                                min: { value: 0.01, message: "Amount must be greater than 0" },
                                max: { value: 1000000, message: "Amount must be 1000000 or less" },
                            })}
                            placeholder="0.00"
                            className="form-control amount-input"
                        />
                    </div>
                    {errors.amount && <span className="form-error">{errors.amount.message}</span>}
                </div>

                <div className="form-group">
                    <label htmlFor="category_id">Category ({selectedType})</label>

                    <select
                        id="category_id"
                        {...register("category_id", {
                            required: "Select a category",
                        })}
                        className="form-control"
                    >
                        <option value="">Select a category</option>

                        {categories.map((category) => (
                            <option key={category.category_id} value={category.category_id}>
                                {category.description}
                            </option>
                        ))}
                    </select>

                    {errors.category_id && <span className="form-error">{errors.category_id.message}</span>}
                </div>

                <div className="form-group">
                    <label htmlFor="name">Description</label>
                    <input
                        type="text"
                        {...register("name", { required: "Description is required" })}
                        placeholder="e.g., Grocery shopping"
                        className="form-control"
                    />
                    {errors.name && <span className="form-error">{errors.name.message}</span>}
                </div>

                <div className="form-group">
                    <label htmlFor="date">Date</label>
                    <input
                        id="date"
                        type="date"
                        {...register('date', { required: 'Date is required' })}
                        className="form-control"
                    />
                    {errors.date && <span className="form-error">{errors.date.message}</span>}
                </div>

                <div className="form-actions">
                    <button type="button" onClick={() => reset()} className="btn btn-cancel">
                        Cancel
                    </button>

                    <button type="submit" className={`btn btn-submit ${selectedType}`}>
                        {selectedType === "expense" ? "Add Expense" : "Add Income"}
                    </button>
                </div>
                                {serverError && <p>{serverError}</p>}
                {successMessage && <p>{successMessage}</p>}
            </form>
        </div>
    );
}

export default TransactionForm;