import { useState } from "react";
import { Tabs, Tab, Box } from "@mui/material";
import "./App.css";
import InstructoresPage from "./pages/InstructoresPage";
import EstudiantesPage from "./pages/EstudiantesPage";
import ClasesPage from "./pages/ClasesPage";

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
        <Tab label="Delete" />
      </Tabs>
      {tabIndex === 0 && <EstudiantesPage />}
      {tabIndex === 1 && <InstructoresPage />}
      {tabIndex === 2 && <ClasesPage />}
      {tabIndex === 3 && <div>Delete Page</div>}
    </Box>
  );
}

export default App;
