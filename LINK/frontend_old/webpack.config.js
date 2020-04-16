module.exports = {
  entry: './src/index.jsx',
  module: {
    rules: [{
      test: /\.(js|jsx)$/,
      exclude: [/\.js$/, /\.html$/, /\.json$/, /\.ejs$/],
      resolve: {
        extensions: [".js", ".jsx"]
      },
      use: {
        loader: "babel-loader"
      },
    }, ]
  }
};