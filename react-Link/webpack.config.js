const path = require("path");
console.log(path.resolve(__dirname, "./frontend/static/frontend/"));
module.exports = {
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
    ],
  },
  entry: {
    index: "./frontend/src/loaders/index.js",
    register: "./frontend/src/loaders/register.js",
    login: "./frontend/src/loaders/login.js",
    createEntry: "./frontend/src/loaders/create_entry.js",
    entries: "./frontend/src/loaders/entries.js",
  },
  output: {
    filename: "[name].js",
    path: path.resolve(__dirname, "./frontend/static/frontend/"),
  },
};
