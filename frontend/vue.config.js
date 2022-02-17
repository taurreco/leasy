const pages = {
  index: "src/main.js",
};

module.exports = {
  publicPath: "/static/vue/",
  outputDir: "./build/static/vue/",
  indexPath: "../../templates/vue_index.html",

  pages: pages,
};

module.rules = [
  {
    // test: /\.s[ac]ss$/i,
    test: /\.(scss)$/,
    use: [{
      // inject CSS to page
      loader: 'style-loader'
    }, {
      // translates CSS into CommonJS modules
      loader: 'css-loader'
    }, {
      // Run postcss actions
      loader: 'postcss-loader',
      options: {
        // `postcssOptions` is needed for postcss 8.x;
        // if you use postcss 7.x skip the key
        postcssOptions: {
          // postcss plugins, can be exported to postcss.config.js
          plugins: function () {
            return [
              require('autoprefixer')
            ];
          }
        }
      }
    }, {
      // compiles Sass to CSS
      loader: 'sass-loader'
    }]
  },
  {
    test: /\.js$/,
    loader: 'babel-loader',
    exclude: /node_modules/
  },
];