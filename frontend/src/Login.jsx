import { useForm } from "react-hook-form";
import { useNavigate, Link } from "react-router";
import { useUser } from "./context/useUser";
import { useState } from "react";
import "./styles/Login.css"

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
    <>
    <div className="login-style">
    <form onSubmit={handleSubmit(onSubmit)} className="login-background">
      {/* <button type="button" onClick={() => navigate("/register")} className="register_button">Register</button> */}
      <h2 className="h2-position">Login</h2>

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
    </div>
    </>
  );
}
