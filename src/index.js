'use strict';

require('./js/jquery.min');
require('./js/main.js');
require('./sass/main.scss');

function importAll(r) {
  return r.keys().map(r);
}

const images = importAll(require.context('./static/images/', false, /\.(png|jpe?g|svg)$/));
