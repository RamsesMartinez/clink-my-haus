const loadGoogleMapsApi = require('load-google-maps-api');

class Map {

  static loadGoogleMapsApi() {
    return loadGoogleMapsApi({ key: process.env.GOOGLEMAPS_KEY });
  }
  static createMap(googleMaps, mapElement, lat, lng) {
    return new googleMaps.Map(mapElement, {
      center: { lat, lng },
      zoom: 12
    });
  }
}
export { Map };