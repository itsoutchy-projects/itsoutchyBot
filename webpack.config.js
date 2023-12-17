const path = require('path');
const webpack = require('webpack');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist'),
  },
  resolve: {
    fallback: {
        "buffer": require.resolve("buffer/"),
        "http": require.resolve("stream-http"),
        "stream": require.resolve("stream-browserify"),
        "assert": require.resolve("assert/"),
        "zlib": require.resolve("browserify-zlib"),
        "util": require.resolve("util/"),
        "url": require.resolve("url/"),
        "console": require.resolve("console-browserify"),
        "crypto": require.resolve("crypto-browserify"),
        "os": require.resolve("os-browserify/browser"),
        "path": require.resolve("path-browserify"),
        "timers": require.resolve("timers-browserify"),
        "process": require.resolve("process/browser")
    }
  },
  plugins: [
    new webpack.NormalModuleReplacementPlugin(/node:/, (resource) => {
      resource.request = resource.request.replace(/^node:/, "");
    }),
  ]
//   externals: {
//     "node:path": "commonjs path",
//     "node:worker_threads": "commonjs path",
//     "node:util": "commonjs path",
//     "node:timers": "commonjs path",
//     "node:timers/promises": "commonjs path",
//     "node:stream": "commonjs path"
//   }
};