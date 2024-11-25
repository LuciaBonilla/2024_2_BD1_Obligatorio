import { useState } from "react";
import { Tabs, Tab, Box } from "@mui/material";
import "./App.css";
import InstructoresPage from "./pages/InstructoresPage";
import EstudiantesPage from "./pages/EstudiantesPage";
import ClasesPage from "./pages/ClasesPage";
import TurnosPage from "./pages/TurnosPage";
import ActividadesPage from "./pages/ActividadesPage";
import ReportesPage from "./pages/ReportesPage";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(true);
  const [tabIndex, setTabIndex] = useState(0);

  const handleTabChange = (event, newValue) => {
    setTabIndex(newValue);
  };

  if (!isLoggedIn) {
    return <div>Please log in to access the app.</div>;
  }

  return (
    <Box sx={{ width: "100%" }}>
      <Tabs value={tabIndex} onChange={handleTabChange} centered>
        <Tab label="Estudiantes" />
        <Tab label="Instructores" />
        <Tab label="Clases" />
        <Tab label="Turnos" />
        <Tab label="Actividades" />
        <Tab label="Reportes" />
      </Tabs>
      {tabIndex === 0 && <EstudiantesPage />}
      {tabIndex === 1 && <InstructoresPage />}
      {tabIndex === 2 && <ClasesPage />}
      {tabIndex === 3 && <TurnosPage />}
      {tabIndex === 4 && <ActividadesPage />}
      {tabIndex === 5 && <ReportesPage />}
    </Box>
  );
}

export default App;
