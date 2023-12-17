const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist'),
  },
  externals: {
    "node:path": "commonjs path",
    "node:worker_threads": "commonjs path",
    "node:util": "commonjs path",
    "node:timers": "commonjs path",
    "node:timers/promises": "commonjs path",
    "node:stream": "commonjs path"
  }
};