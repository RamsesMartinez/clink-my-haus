import { tns } from "tiny-slider/src/tiny-slider"
import 'lightbox2';

// Google Maps API
let mapElement = document.getElementById('map');
let lat = Number.parseFloat(mapElement.getAttribute('data-latitude'));
let lng = Number.parseFloat(mapElement.getAttribute('data-longitude'));

function initMap() {
  let location = {lat, lng};
  // The map, centered
  let map = new google.maps.Map(
      document.getElementById('map'), {zoom: 15, center: location});
  // Creates the Marker
  new google.maps.Marker({position: location, map: map});
}

window.initMap = initMap;


// Tiny Gallery
tns({
    container: '.img-carousel-slider',
    autoWidth: true,
    autoHeight: false,
    items: 1.3,
    gutter: 5,
    rewind: true,
    mouseDrag: true,
    swipeAngle: false,
    center: true,
    speed: 400,
    arrowKeys: true,
    controlsText: ['Anterior', 'Siguiente'],
    controlsPosition: 'bottom'
});