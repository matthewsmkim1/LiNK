import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import CssBaseline from "@material-ui/core/CssBaseline";
import clsx from "clsx";
import Card from "@material-ui/core/Card";
import CardHeader from "@material-ui/core/CardHeader";
import CardMedia from "@material-ui/core/CardMedia";
import CardContent from "@material-ui/core/CardContent";
import CardActions from "@material-ui/core/CardActions";
import Collapse from "@material-ui/core/Collapse";
import Avatar from "@material-ui/core/Avatar";
import IconButton from "@material-ui/core/IconButton";
import Typography from "@material-ui/core/Typography";
import { red } from "@material-ui/core/colors";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import MoreVertIcon from "@material-ui/icons/MoreVert";
import TopBar from "../layout/TopBar";
import Footer from "../layout/Footer";
import TextField from "@material-ui/core/TextField";
import Fab from "@material-ui/core/Fab";
import Image from "@material-ui/icons/Image";
import Movie from "@material-ui/icons/Movie";
import Button from "@material-ui/core/Button";
import Checkbox from "@material-ui/core/Checkbox";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import FormControl from "@material-ui/core/FormControl";
import FormLabel from "@material-ui/core/FormLabel";
import Box from "@material-ui/core/Box";

const useStyles = makeStyles((theme) => ({
  root: {
    maxWidth: 345,
  },
  media: {
    width: "500",
    height: "500",
    paddingTop: "45.25%", // 16:9
  },
  expand: {
    transform: "rotate(0deg)",
    marginLeft: "auto",
    transition: theme.transitions.create("transform", {
      duration: theme.transitions.duration.shortest,
    }),
  },
  expandOpen: {
    transform: "rotate(180deg)",
  },
  avatar: {
    backgroundColor: red[500],
  },
  appBar: {
    position: "relative",
  },
  layout: {
    width: "auto",
    marginLeft: theme.spacing(2),
    marginRight: theme.spacing(2),
    [theme.breakpoints.up(600 + theme.spacing(2) * 2)]: {
      width: 600,
      marginLeft: "auto",
      marginRight: "auto",
    },
  },
  paper: {
    marginTop: theme.spacing(3),
    marginBottom: theme.spacing(3),
    padding: theme.spacing(2),
    [theme.breakpoints.up(600 + theme.spacing(3) * 2)]: {
      marginTop: theme.spacing(6),
      marginBottom: theme.spacing(6),
      padding: theme.spacing(3),
    },
  },
  buttons: {
    display: "flex",
    justifyContent: "flex-end",
  },
  button: {
    marginTop: theme.spacing(3),
    marginLeft: theme.spacing(1),
  },
  toolbar: {
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    padding: theme.spacing(0, 1),
    // necessary for content to be below app bar
    ...theme.mixins.toolbar,
  },
  content: {
    flexGrow: 1,
    padding: theme.spacing(3),
  },
  cardStyle: {
    // maxWidth: 500,
    display: "block",
    width: "65vw",
    transitionDuration: "0.3s",
    height: "55vw",
  },
  titleField: {
    margin: theme.spacing(1),
    maxWidth: "60vw",
    width: "100ch",
    height: "20ch",
  },
  entryParagraph: {
    margin: theme.spacing(1),
    maxWidth: "60vw",
    width: "200ch",
    height: "200ch",
  },
  extendedIcon: {
    marginRight: theme.spacing(10),
  },
}));

const EntryCard = (props) => {
  const classes = useStyles();
  const [expanded, setExpanded] = React.useState(true);
  const [mediaUploaded, setMediaUploaded] = React.useState(false);
  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

  return (
    <Card className={classes.cardStyle}>
      <CardContent>
        <TextField
          label={"title"}
          className={classes.titleField}
          variant="filled"
        />
      </CardContent>
      <CardMedia
        className={classes.media}
        image="https://source.unsplash.com/random"
      />
      <CardActions disableSpacing>
        <Fab variant="extended" className={classes.extendedIcon}>
          <Image />
          Upload Photo
        </Fab>
        <Fab variant="extended" className={classes.extendedIcon}>
          <Movie />
          Upload video
        </Fab>
        <IconButton
          className={clsx(classes.expand, {
            [classes.expandOpen]: expanded,
          })}
          onClick={handleExpandClick}
          aria-expanded={expanded}
          aria-label="show more"
        >
          <ExpandMoreIcon />
        </IconButton>
      </CardActions>
      <Collapse in={expanded} timeout="auto" unmountOnExit>
        <CardContent>
          <TextField
            label="write here!"
            className={classes.entryParagraph}
            multiline
            defaultValue="The greatest post ever!"
          />
        </CardContent>
      </Collapse>
    </Card>
  );
};
let GROUPS = ["group1", "group2", "group3"];
const SelectGroups = (props) => {
  const [value, setValue] = React.useState("None");

  const handleChange = (event) => {
    setValue(event.target.value);
  };

  const classes = useStyles();

  const group_create_func = GROUPS.map((item) => {
    return (
      <FormControlLabel value={item} control={<Checkbox />} label={item} />
    );
  });

  return (
    <FormControl component="fieldset">
      <FormLabel component="legend" margin="20" padding="15">
        Groups
      </FormLabel>
      <RadioGroup
        aria-label="Groups"
        value={value}
        onChange={handleChange}
        height="100"
        width="100"
      >
        <FormControlLabel value="None" control={<Checkbox />} label="None" />
        {group_create_func}
      </RadioGroup>
      <Button
        type="submit"
        variant="outlined"
        color="primary"
        className={classes.button}
      >
        Submit
      </Button>
    </FormControl>
  );
};

const CreateEntry = (props) => {
  const classes = useStyles();

  return (
    <React.Fragment>
      <CssBaseline />
      <TopBar />
      <main className={classes.content}>
        <main className={classes.toolbar}>
          <EntryCard />
        </main>
        <main className={classes.toolbar} margin="20" padding="50px">
          <Box mx="auto" p={5}>
            <SelectGroups />
          </Box>
        </main>
      </main>
      <Footer />
    </React.Fragment>
  );
};

export default CreateEntry;
