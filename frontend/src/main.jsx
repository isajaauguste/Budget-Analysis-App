import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router";
import { UserProvider } from "../src/context/userProvider.jsx";
import "./index.css";
import App from "./App.jsx";
import UserGate from "./UserGate.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <BrowserRouter>
    <UserProvider>
      <UserGate>
          <App />
      </UserGate>
    </UserProvider>
    </BrowserRouter>
  </StrictMode>
);
