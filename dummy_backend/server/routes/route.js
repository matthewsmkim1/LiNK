const errors = require('restify-errors');
const Base = require('../schemas/base.js');


module.exports = server => {
  // get objects
  server.get('/base', async (req, res, next) => {
    try {
      const objects = await Base.find({});
      res.send(customers);
      next();
    } catch (err) {
      return next(new errors.InvalidContentError(err));
    }

  });

  //get a single object
  server.get('/base/:id', async (req, res, next) => {

    try {
      const obj = await Base.findById(req.params.id);
      res.send(obj);
      next();
    } catch (err) {
      return next(new errors.ResourceNotFoundError(`can't find id ${req.params.id}`));
    }
  });


  // add an object
  server.post('/base', async (req, res, next) => {
    if (!req.is('application/json')) {
      return next(new errors.InvalidContentError("expects application/json"));
    }
    let fields = req.body; // include fields here
    // const {field1, field2, field} = req.body;
    const base_added = new Base(fields);

    try {
      //check for json
      const newObjAdde = await base_added.save();
      res.send(201);
      next();
    } catch (err) {
      return next(new errors.InternalError(err.message));
    }
  });

  // update an object
  server.put('/base/:id', async (req, res, next) => {

    if (!req.is('application/json')) {
      return next(new errors.InvalidContentError('Expects application/json'));
    }
    try {
      let id = {
        _id: req.params.id
      };
      let data = req.body;
      const updatedObject = await Base.findOneAndUpdate(id, data);
      res.send(201);
      next();

    } catch (err) {
      return next(new errors.ResourceNotFoundError(`no object with id ${req.params.id}`));
    }
  });

  // delete an object
  server.del('/base/:id', async (req, res, next) => {

    if (!req.is('application/json')) {
      return next(new errors.InvalidContentError('Expects application/json'));
    }
    try {
      let id = {
        _id: req.params.id
      };
      const updatedObject = await Base.findOneAndRemove(id);
      res.send(201);
      next();

    } catch (err) {
      return next(new errors.ResourceNotFoundError(`no object with id ${req.params.id}`));
    }
  });
};