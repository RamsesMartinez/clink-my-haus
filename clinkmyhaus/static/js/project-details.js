/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./src/js/project-details.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./node_modules/load-google-maps-api/index.js":
/*!****************************************************!*\
  !*** ./node_modules/load-google-maps-api/index.js ***!
  \****************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("const API_URL = 'https://maps.googleapis.com/maps/api/js'\nconst CALLBACK_NAME = '__googleMapsApiOnLoadCallback'\n\nconst optionsKeys = ['channel', 'client', 'key', 'language', 'region', 'v']\n\nlet promise = null\n\nmodule.exports = function (options = {}) {\n  promise =\n    promise ||\n    new Promise(function (resolve, reject) {\n      // Reject the promise after a timeout\n      const timeoutId = setTimeout(function () {\n        window[CALLBACK_NAME] = function () {} // Set the on load callback to a no-op\n        reject(new Error('Could not load the Google Maps API'))\n      }, options.timeout || 10000)\n\n      // Hook up the on load callback\n      window[CALLBACK_NAME] = function () {\n        if (timeoutId !== null) {\n          clearTimeout(timeoutId)\n        }\n        resolve(window.google.maps)\n        delete window[CALLBACK_NAME]\n      }\n\n      // Prepare the `script` tag to be inserted into the page\n      const scriptElement = document.createElement('script')\n      const params = [`callback=${CALLBACK_NAME}`]\n      optionsKeys.forEach(function (key) {\n        if (options[key]) {\n          params.push(`${key}=${options[key]}`)\n        }\n      })\n      if (options.libraries && options.libraries.length) {\n        params.push(`libraries=${options.libraries.join(',')}`)\n      }\n      scriptElement.src = `${options.apiUrl || API_URL}?${params.join('&')}`\n\n      // Insert the `script` tag\n      document.body.appendChild(scriptElement)\n    })\n  return promise\n}\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9ub2RlX21vZHVsZXMvbG9hZC1nb29nbGUtbWFwcy1hcGkvaW5kZXguanMuanMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8vLi9ub2RlX21vZHVsZXMvbG9hZC1nb29nbGUtbWFwcy1hcGkvaW5kZXguanM/YTcwOSJdLCJzb3VyY2VzQ29udGVudCI6WyJjb25zdCBBUElfVVJMID0gJ2h0dHBzOi8vbWFwcy5nb29nbGVhcGlzLmNvbS9tYXBzL2FwaS9qcydcbmNvbnN0IENBTExCQUNLX05BTUUgPSAnX19nb29nbGVNYXBzQXBpT25Mb2FkQ2FsbGJhY2snXG5cbmNvbnN0IG9wdGlvbnNLZXlzID0gWydjaGFubmVsJywgJ2NsaWVudCcsICdrZXknLCAnbGFuZ3VhZ2UnLCAncmVnaW9uJywgJ3YnXVxuXG5sZXQgcHJvbWlzZSA9IG51bGxcblxubW9kdWxlLmV4cG9ydHMgPSBmdW5jdGlvbiAob3B0aW9ucyA9IHt9KSB7XG4gIHByb21pc2UgPVxuICAgIHByb21pc2UgfHxcbiAgICBuZXcgUHJvbWlzZShmdW5jdGlvbiAocmVzb2x2ZSwgcmVqZWN0KSB7XG4gICAgICAvLyBSZWplY3QgdGhlIHByb21pc2UgYWZ0ZXIgYSB0aW1lb3V0XG4gICAgICBjb25zdCB0aW1lb3V0SWQgPSBzZXRUaW1lb3V0KGZ1bmN0aW9uICgpIHtcbiAgICAgICAgd2luZG93W0NBTExCQUNLX05BTUVdID0gZnVuY3Rpb24gKCkge30gLy8gU2V0IHRoZSBvbiBsb2FkIGNhbGxiYWNrIHRvIGEgbm8tb3BcbiAgICAgICAgcmVqZWN0KG5ldyBFcnJvcignQ291bGQgbm90IGxvYWQgdGhlIEdvb2dsZSBNYXBzIEFQSScpKVxuICAgICAgfSwgb3B0aW9ucy50aW1lb3V0IHx8IDEwMDAwKVxuXG4gICAgICAvLyBIb29rIHVwIHRoZSBvbiBsb2FkIGNhbGxiYWNrXG4gICAgICB3aW5kb3dbQ0FMTEJBQ0tfTkFNRV0gPSBmdW5jdGlvbiAoKSB7XG4gICAgICAgIGlmICh0aW1lb3V0SWQgIT09IG51bGwpIHtcbiAgICAgICAgICBjbGVhclRpbWVvdXQodGltZW91dElkKVxuICAgICAgICB9XG4gICAgICAgIHJlc29sdmUod2luZG93Lmdvb2dsZS5tYXBzKVxuICAgICAgICBkZWxldGUgd2luZG93W0NBTExCQUNLX05BTUVdXG4gICAgICB9XG5cbiAgICAgIC8vIFByZXBhcmUgdGhlIGBzY3JpcHRgIHRhZyB0byBiZSBpbnNlcnRlZCBpbnRvIHRoZSBwYWdlXG4gICAgICBjb25zdCBzY3JpcHRFbGVtZW50ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc2NyaXB0JylcbiAgICAgIGNvbnN0IHBhcmFtcyA9IFtgY2FsbGJhY2s9JHtDQUxMQkFDS19OQU1FfWBdXG4gICAgICBvcHRpb25zS2V5cy5mb3JFYWNoKGZ1bmN0aW9uIChrZXkpIHtcbiAgICAgICAgaWYgKG9wdGlvbnNba2V5XSkge1xuICAgICAgICAgIHBhcmFtcy5wdXNoKGAke2tleX09JHtvcHRpb25zW2tleV19YClcbiAgICAgICAgfVxuICAgICAgfSlcbiAgICAgIGlmIChvcHRpb25zLmxpYnJhcmllcyAmJiBvcHRpb25zLmxpYnJhcmllcy5sZW5ndGgpIHtcbiAgICAgICAgcGFyYW1zLnB1c2goYGxpYnJhcmllcz0ke29wdGlvbnMubGlicmFyaWVzLmpvaW4oJywnKX1gKVxuICAgICAgfVxuICAgICAgc2NyaXB0RWxlbWVudC5zcmMgPSBgJHtvcHRpb25zLmFwaVVybCB8fCBBUElfVVJMfT8ke3BhcmFtcy5qb2luKCcmJyl9YFxuXG4gICAgICAvLyBJbnNlcnQgdGhlIGBzY3JpcHRgIHRhZ1xuICAgICAgZG9jdW1lbnQuYm9keS5hcHBlbmRDaGlsZChzY3JpcHRFbGVtZW50KVxuICAgIH0pXG4gIHJldHVybiBwcm9taXNlXG59XG4iXSwibWFwcGluZ3MiOiJBQUFBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7Iiwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///./node_modules/load-google-maps-api/index.js\n");

/***/ }),

/***/ "./node_modules/slick-carousel/slick/slick-theme.css":
/*!***********************************************************!*\
  !*** ./node_modules/slick-carousel/slick/slick-theme.css ***!
  \***********************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("// extracted by mini-css-extract-plugin//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9ub2RlX21vZHVsZXMvc2xpY2stY2Fyb3VzZWwvc2xpY2svc2xpY2stdGhlbWUuY3NzLmpzIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vLy4vbm9kZV9tb2R1bGVzL3NsaWNrLWNhcm91c2VsL3NsaWNrL3NsaWNrLXRoZW1lLmNzcz9mNDQ5Il0sInNvdXJjZXNDb250ZW50IjpbIi8vIGV4dHJhY3RlZCBieSBtaW5pLWNzcy1leHRyYWN0LXBsdWdpbiJdLCJtYXBwaW5ncyI6IkFBQUEiLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///./node_modules/slick-carousel/slick/slick-theme.css\n");

/***/ }),

/***/ "./node_modules/slick-carousel/slick/slick.css":
/*!*****************************************************!*\
  !*** ./node_modules/slick-carousel/slick/slick.css ***!
  \*****************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("// extracted by mini-css-extract-plugin//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9ub2RlX21vZHVsZXMvc2xpY2stY2Fyb3VzZWwvc2xpY2svc2xpY2suY3NzLmpzIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vLy4vbm9kZV9tb2R1bGVzL3NsaWNrLWNhcm91c2VsL3NsaWNrL3NsaWNrLmNzcz9mMGU2Il0sInNvdXJjZXNDb250ZW50IjpbIi8vIGV4dHJhY3RlZCBieSBtaW5pLWNzcy1leHRyYWN0LXBsdWdpbiJdLCJtYXBwaW5ncyI6IkFBQUEiLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///./node_modules/slick-carousel/slick/slick.css\n");

/***/ }),

/***/ "./src/js/map.js":
/*!***********************!*\
  !*** ./src/js/map.js ***!
  \***********************/
/*! exports provided: Map */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"Map\", function() { return Map; });\nconst loadGoogleMapsApi = __webpack_require__(/*! load-google-maps-api */ \"./node_modules/load-google-maps-api/index.js\");\r\n\r\nclass Map {\r\n\r\n  static loadGoogleMapsApi() {\r\n    return loadGoogleMapsApi({ key: \"AIzaSyAi8gozS1FGHQEV3rdJExP2aigb3GgwbGo\" });\r\n  }\r\n  static createMap(googleMaps, mapElement, lat, lng) {\r\n    return new googleMaps.Map(mapElement, {\r\n      center: { lat, lng },\r\n      zoom: 12\r\n    });\r\n  }\r\n}\r\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvanMvbWFwLmpzLmpzIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vLy4vc3JjL2pzL21hcC5qcz8yNjc5Il0sInNvdXJjZXNDb250ZW50IjpbImNvbnN0IGxvYWRHb29nbGVNYXBzQXBpID0gcmVxdWlyZSgnbG9hZC1nb29nbGUtbWFwcy1hcGknKTtcclxuXHJcbmNsYXNzIE1hcCB7XHJcblxyXG4gIHN0YXRpYyBsb2FkR29vZ2xlTWFwc0FwaSgpIHtcclxuICAgIHJldHVybiBsb2FkR29vZ2xlTWFwc0FwaSh7IGtleTogcHJvY2Vzcy5lbnYuR09PR0xFTUFQU19LRVkgfSk7XHJcbiAgfVxyXG4gIHN0YXRpYyBjcmVhdGVNYXAoZ29vZ2xlTWFwcywgbWFwRWxlbWVudCwgbGF0LCBsbmcpIHtcclxuICAgIHJldHVybiBuZXcgZ29vZ2xlTWFwcy5NYXAobWFwRWxlbWVudCwge1xyXG4gICAgICBjZW50ZXI6IHsgbGF0LCBsbmcgfSxcclxuICAgICAgem9vbTogMTJcclxuICAgIH0pO1xyXG4gIH1cclxufVxyXG5leHBvcnQgeyBNYXAgfTsiXSwibWFwcGluZ3MiOiJBQUFBO0FBQUE7QUFBQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOyIsInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///./src/js/map.js\n");

/***/ }),

/***/ "./src/js/project-details.js":
/*!***********************************!*\
  !*** ./src/js/project-details.js ***!
  \***********************************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var slick_carousel_slick_slick_css__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! slick-carousel/slick/slick.css */ \"./node_modules/slick-carousel/slick/slick.css\");\n/* harmony import */ var slick_carousel_slick_slick_css__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(slick_carousel_slick_slick_css__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var slick_carousel_slick_slick_theme_css__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! slick-carousel/slick/slick-theme.css */ \"./node_modules/slick-carousel/slick/slick-theme.css\");\n/* harmony import */ var slick_carousel_slick_slick_theme_css__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(slick_carousel_slick_slick_theme_css__WEBPACK_IMPORTED_MODULE_1__);\n/* harmony import */ var _map__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./map */ \"./src/js/map.js\");\n\r\n\r\n\r\n\r\n$(document).ready(function(){\r\n\r\n    $('.slider-for').slick({\r\n        slidesToShow: 1,\r\n        slidesToScroll: 1,\r\n        arrows: false,\r\n        fade: true,\r\n        speed: 750,\r\n        asNavFor: '.slider-nav'\r\n    });\r\n\r\n    $('.slider-nav').slick({\r\n        slidesToShow: 3,\r\n        slidesToScroll: 1,\r\n        asNavFor: '.slider-for',\r\n        dots: true,\r\n        centerMode: true,\r\n        focusOnSelect: true,\r\n        autoplay: true,\r\n        autoplaySpeed: 2000\r\n    });\r\n});\r\n\r\ndocument.addEventListener(\"DOMContentLoaded\", function() {\r\n  let mapElement = document.getElementById('map');\r\n\r\n  _map__WEBPACK_IMPORTED_MODULE_2__[\"Map\"].loadGoogleMapsApi().then(function(googleMaps) {\r\n    _map__WEBPACK_IMPORTED_MODULE_2__[\"Map\"].createMap(googleMaps, mapElement, 9, 10);\r\n  });\r\n});//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvanMvcHJvamVjdC1kZXRhaWxzLmpzLmpzIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vLy4vc3JjL2pzL3Byb2plY3QtZGV0YWlscy5qcz85ZjVjIl0sInNvdXJjZXNDb250ZW50IjpbImltcG9ydCAnc2xpY2stY2Fyb3VzZWwvc2xpY2svc2xpY2suY3NzJztcclxuaW1wb3J0ICdzbGljay1jYXJvdXNlbC9zbGljay9zbGljay10aGVtZS5jc3MnO1xyXG5pbXBvcnQgeyBNYXAgfSBmcm9tICcuL21hcCc7XHJcblxyXG4kKGRvY3VtZW50KS5yZWFkeShmdW5jdGlvbigpe1xyXG5cclxuICAgICQoJy5zbGlkZXItZm9yJykuc2xpY2soe1xyXG4gICAgICAgIHNsaWRlc1RvU2hvdzogMSxcclxuICAgICAgICBzbGlkZXNUb1Njcm9sbDogMSxcclxuICAgICAgICBhcnJvd3M6IGZhbHNlLFxyXG4gICAgICAgIGZhZGU6IHRydWUsXHJcbiAgICAgICAgc3BlZWQ6IDc1MCxcclxuICAgICAgICBhc05hdkZvcjogJy5zbGlkZXItbmF2J1xyXG4gICAgfSk7XHJcblxyXG4gICAgJCgnLnNsaWRlci1uYXYnKS5zbGljayh7XHJcbiAgICAgICAgc2xpZGVzVG9TaG93OiAzLFxyXG4gICAgICAgIHNsaWRlc1RvU2Nyb2xsOiAxLFxyXG4gICAgICAgIGFzTmF2Rm9yOiAnLnNsaWRlci1mb3InLFxyXG4gICAgICAgIGRvdHM6IHRydWUsXHJcbiAgICAgICAgY2VudGVyTW9kZTogdHJ1ZSxcclxuICAgICAgICBmb2N1c09uU2VsZWN0OiB0cnVlLFxyXG4gICAgICAgIGF1dG9wbGF5OiB0cnVlLFxyXG4gICAgICAgIGF1dG9wbGF5U3BlZWQ6IDIwMDBcclxuICAgIH0pO1xyXG59KTtcclxuXHJcbmRvY3VtZW50LmFkZEV2ZW50TGlzdGVuZXIoXCJET01Db250ZW50TG9hZGVkXCIsIGZ1bmN0aW9uKCkge1xyXG4gIGxldCBtYXBFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ21hcCcpO1xyXG5cclxuICBNYXAubG9hZEdvb2dsZU1hcHNBcGkoKS50aGVuKGZ1bmN0aW9uKGdvb2dsZU1hcHMpIHtcclxuICAgIE1hcC5jcmVhdGVNYXAoZ29vZ2xlTWFwcywgbWFwRWxlbWVudCwgOSwgMTApO1xyXG4gIH0pO1xyXG59KTsiXSwibWFwcGluZ3MiOiJBQUFBO0FBQUE7QUFBQTtBQUFBO0FBQUE7QUFBQTtBQUFBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBIiwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///./src/js/project-details.js\n");

/***/ })

/******/ });