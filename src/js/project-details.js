import { Map } from './map';
import { tns } from "tiny-slider/src/tiny-slider"
require('tiny-slider/src/tiny-slider.scss');

// Google Maps API
document.addEventListener("DOMContentLoaded", function() {
    let mapElement = document.getElementById('map');
    let latitude = Number.parseFloat(mapElement.getAttribute('data-latitude'));
    let longitude = Number.parseFloat(mapElement.getAttribute('data-longitude'));

    Map.loadGoogleMapsApi().then(function(googleMaps) {
        Map.createMap(googleMaps, mapElement, latitude, longitude);
    });
});

// Tiny Gallery
const slider = tns({
    container: '.img-carousel-slider',
    autoWidth: true,
    autoHeight: false,
    items: 1.3,
    gutter: 5,
    mouseDrag: true,
    swipeAngle: false,
    center: true,
    speed: 400,
    arrowKeys: true,
    controlsText: ['Anterior', 'Siguiente'],
    lazyload: true,
    controlsPosition: 'bottom'
});