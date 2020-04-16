import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import TopNav from "../components/TopNav.jsx";
import SideMenu from "../components/SideMenu.jsx";
import Footer from "../components/Footer.jsx";
import MainContent from "../components/MainContent.jsx";

const useStyles = makeStyles((theme) => ({
  root: {
    display: "flex",
  },
}));

function LandingPage() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <TopMenu />
      <SideMenu />
      <MainContent />
      <Footer />
    </div>
  );
}

export default LandingPage;
