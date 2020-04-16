import React from "react";
import ReactDOM from "react-dom";
// import './index.css';
import LandingPage from "./pages/LandingPage.jsx";

target_node = document.getElementById("root");
console.log(target_node);
ReactDOM.render(<div>hello</div>, target_node);

function hello() {
  return "hellp";
}
