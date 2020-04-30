import React from "react";
import ReactDOM from "react-dom";
import Entries from "../components/layout/Entries";

var new_arr = [];
arrTop.map((element, index) => {
  new_arr.push([element, arrBottom[index]]);
});

ReactDOM.render(
  <Entries zipped={new_arr} />,

  document.getElementById("app")
);
