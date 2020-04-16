const express = require('express');
const app = express();
const axios = require('axios');
var path = require('path');



app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname + '/../public/index.html'));
});



app.listen(8000, () => {
  console.log('server started on port 8000');
});