const mongoose = require('mongoose');
const restify = require('restify');
const config = require('./config.js');



const server = restify.createServer();


//middleware
server.use(restify.plugins.bodyParser());

server.get('/', (req, res) => {
  res.send("it's working :)")
});

server.listen(config.PORT, () => {
  mongoose.set('useFindAndModify', false);
  mongoose.connect(config.MONGODB_URI, {
    useNewUrlParser: true
  }, () => console.log("connected to db"));
  console.log('Server running...');
});

const db = mongoose.connection;

if (db == null) {
  throw error("not connected to db");
}

db.on('error', (err) => console.log(err));

db.on('open', () => {
  console.log("db is opened");
  require('./routes/route.js');
});