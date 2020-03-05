const mongoose = require('mongoose');
const timestamp = require('mongoose-timestamp');



const Base_Schema = new mongoose.Schema({


  strField1: {
    type: String,
  },
  numField1: {
    type: Number
  },

  date: {
    type: Date,
    default: Date.now
  },

  boolfield1: {
    type: Boolean
  },

  buff: {
    type: Buffer
  },

  mixy: {
    type: {
      foo: String
    }
  },

  objId: {
    type: mongoose.ObjectId
  },

  arr: {
    type: Array
  },

  mappy: {
    type: Map
  }
});


Base_Schema.plugin(timestamp);


const Base = mongoose.model('Base', Base_Schema);

module.exports = Base;