const path = require('path');

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
        "util": require.resolve("util/")
    }
  }
//   externals: {
//     "node:path": "commonjs path",
//     "node:worker_threads": "commonjs path",
//     "node:util": "commonjs path",
//     "node:timers": "commonjs path",
//     "node:timers/promises": "commonjs path",
//     "node:stream": "commonjs path"
//   }
};