const path = require( 'path' );

const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const HtmlWebPackPlugin = require( 'html-webpack-plugin' );
const CopyWebpackPlugin = require('copy-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');

module.exports = (env) => {
  const isProduction = env.production === true

  let config = {
    entry: [
      './src/index.js',
      './src/styles/main.css'
    ],
    output: {
      filename: isProduction ? 'bundle.[fullhash].js': 'bundle.js',
      path: path.resolve(__dirname, 'dist'),
      hashFunction: "xxhash64"
    },
    resolve: {
      modules: [
        path.resolve(__dirname, 'src'),
        'node_modules'
      ]
    },
    mode: isProduction ? "production" : 'development',
    devServer: {
      host: "0.0.0.0",
      port: 5000,
      hot: true
    },
    module: {
      rules: [
        {
          test: /\.(js|jsx)$/,
          exclude: /node_modules/,
          use: {
            loader: "babel-loader"
          }
        },
        {
          test: /\.css$/,
          use: [
            isProduction ? MiniCssExtractPlugin.loader : 'style-loader', 'css-loader', 'postcss-loader'
          ]
        },
        {
          test: /\.(png|jpg)$/,
          type: 'asset/resource',
          generator: {
            filename: './images/[name][ext]',
          }
        },
        {
          test: /\.(ttf|otf|eot|svg|woff(2)?)(\?[a-z0-9]+)?$/,
          type: 'asset/resource',
          generator: {
            filename: './fonts/[name][ext]',
          }
        }
      ]
    },
    plugins: [
      new CleanWebpackPlugin({
        cleanAfterEveryBuildPatterns: ['dist']
      }),
      new HtmlWebPackPlugin({
        filename: "./index.html",
        template: "./src/index.html"
      }),
      new CopyWebpackPlugin({
        patterns: [
          { from: './src/runtime-config.js' }
        ]
      })
    ]
  }

  if(isProduction) {
    config.plugins.unshift(
      new MiniCssExtractPlugin({
        filename: 'styles.[fullhash].css'
      })
    )
  }

  return config
}
