import { useForm } from "react-hook-form";
import { useNavigate } from "react-router";
import { useState } from "react";
import api from "./lib/axios";

export default function Register() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const navigate = useNavigate();
  const [serverError, setServerError] = useState(null);
  const [successMessage, setSuccessMessage] = useState(null);

  const onSubmit = async (data) => {
    setServerError(null);
    setSuccessMessage(null);

    try {
      await api.post("/users", data);

      setSuccessMessage("User registered successfully");
      navigate("/");
    } catch (err) {
      const message = err?.response?.data?.message || "Registration failed";

      setServerError(message);
    }
  };

  const password = watch("password");

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <h2>Register</h2>

      {serverError && <p>{serverError}</p>}

      {successMessage && <p>{successMessage}</p>}

      <input
        type="text"
        placeholder="Username"
        {...register("username", {
          required: "Username is required",
        })}
      />

      <input
        type="email"
        placeholder="Email"
        {...register("email", {
          required: "Email is required",
        })}
      />
      {errors.email && <p>{errors.email.message}</p>}

      <input
        type="password"
        placeholder="Password"
        {...register("password", {
          required: "Password is required",
        })}
      />
      {errors.password && <p>{errors.password.message}</p>}

      <button type="submit">Register</button>
    </form>
  );
}
