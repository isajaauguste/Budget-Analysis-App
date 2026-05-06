import { useForm } from "react-hook-form";
import { useNavigate } from "react-router";
import { useUser } from "./context/useUser";
import { useState } from "react";

export default function Login() {

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();
  const { login } = useUser();
  const navigate = useNavigate();
  const [serverError, setServerError] = useState(null);

  const onSubmit = async (data) => {
    setServerError(null);

    try {
      const loggedUser = await login(data);

      if (loggedUser.role === "admin") {
        navigate("/admin");
      } else {
        navigate("/dashboard");
      }
    } catch (err) {
      const message = err?.response?.data?.message || "Login failed";

      setServerError(message);
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <h2>Login</h2>

      {serverError && <p>{serverError}</p>}

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

      <button type="submit">Login</button>
    </form>
  );
}
