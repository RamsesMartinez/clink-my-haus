const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const autoprefixer = require('autoprefixer');


module.exports = env => {
    const {NODE_ENV} = env;
    return  {
        entry: {
            'bundle': './src/index.js',
            'project-details': './src/js/project-details.js',
        },
        output: {
            filename: '[name].js',
            path: path.resolve(__dirname, 'clinkmyhaus/static/js')
        },
        devtool: 'source-map',
        module: {
            rules: [
                {
                    test: /\.js.$/,
                    exclude: /node_modules/,
                    loader: "babel-loader"
                },
                {
                    test: /\.(sa|sc|c)ss$/,
                    use: [
                        MiniCssExtractPlugin.loader,
                        'css-loader',
                        {
                            loader: 'postcss-loader',
                            options: {
                                autoprefixer: {
                                    browser: ["last 2 versions"]
                                },
                                plugins: () => [
                                    autoprefixer
                                ]
                            }
                        },
                        'sass-loader',
                    ],
                },
                {
                    test: /\.(jpg|png|gif|svg)$/,
                    exclude:  /fonts/,
                    use: [
                        {
                            loader: 'file-loader',
                            options: {
                                name: '[name].[ext]',
                                outputPath: '../images/',
                                useRelativePath: true
                            }
                        },
                        {
                            loader: 'image-webpack-loader',
                            options: {
                                mozjpeg: {
                                    progressive: true,
                                    quality: 65
                                },
                                // optipng.enabled: false will disable optipng
                                optipng: {
                                    enabled: false,
                                },
                                pngquant: {
                                    quality: '65-90',
                                    speed: 4
                                },
                                gifsicle: {
                                    interlaced: false,
                                },
                                // the webp option will enable WEBP
                                webp: {
                                    quality: 75
                                }
                            }
                        }
                    ]
                },
                {
                    test: /\.(woff(2)?|ttf|eot|svg)(\?v=\d+\.\d+\.\d+)?$/,
                    exclude:  /images/,
                    use: [
                        {
                            loader: 'file-loader',
                            options: {
                                name: '[name].[ext]',
                                outputPath: '../fonts/'
                            }
                        }
                    ]
                },
            ],
        },
        plugins: [
            new MiniCssExtractPlugin({
                filename: "../css/[name]-styles.css",
                chunkFilename: "[id].css"
            })
        ],
        watch: NODE_ENV === 'development'
    }
};
