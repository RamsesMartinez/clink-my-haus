'use strict';

import $ from 'jquery';
require('./js/main.js');
require('./sass/main.scss');
require('./js/fonts');

// Load static images
window.$ = window.jQuery = $;
function importAll(r) {
  return r.keys().map(r);
}

importAll(require.context('./static/images/', false, /\.(png|jpe?g|svg)$/));
