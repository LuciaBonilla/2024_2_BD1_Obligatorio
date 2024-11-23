import { useState } from "react";
import { Tabs, Tab } from "@mui/material";
import Instructores from "./pages/InstructoresPage";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);
  const [selectedTab, setSelectedTab] = useState(0);

  const handleTabChange = (event: React.SyntheticEvent, newValue: number) => {
    setSelectedTab(newValue);
  };

  return (
    <>
      <h1>UCU SNOW SPORTS</h1>
      <Tabs
        value={selectedTab}
        onChange={handleTabChange}
        aria-label="basic tabs example"
      >
        <Tab label="Instructores" />
        <Tab label="Page 1" />
        <Tab label="Page 2" />
      </Tabs>
      {selectedTab === 0 && <Instructores/>}
      {selectedTab === 1 && <div>Page 1 Content</div>}
      {selectedTab === 2 && <div>Page 2 Content</div>}
    </>
  );
}

export default App;
