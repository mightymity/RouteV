from PyQt4.QtWebKit import *
#from PyQt4.QtGui import *


class CalWidget(QWebView):
    """
    This is the GMAPS Widget class.
    """

    def __init__(self):

        super().__init__()

        self.html='''<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Waypoints in directions</title>
    <style>
      #right-panel {
        font-family: 'Roboto','sans-serif';
        line-height: 30px;
        padding-left: 10px;
      }

      #right-panel select, #right-panel input {
        font-size: 15px;
      }

      #right-panel select {
        width: 100%;
      }

      #right-panel i {
        font-size: 12px;
      }
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
      #map {
        height: 100%;
        float: left;
        width: 100%;
        height: 100%;
      }

    </style>
  </head>
  <body>
    <div id="map"></div>

    </div>
    <script>
      function initMap() {
        var directionsService = new google.maps.DirectionsService;
        var directionsDisplay = new google.maps.DirectionsRenderer;
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 6,
          center: {lat: 41.85, lng: -87.65}
        });


        directionsDisplay.setMap(map);

          calculateAndDisplayRoute(directionsService, directionsDisplay);

      }

      function calculateAndDisplayRoute(directionsService, directionsDisplay) {
        var waypts = [];
            waypts.push({
              location: {placeId: 'ChIJ4VX0ws-e4jARBGaQ2IACrcQ'},
              stopover: true
            });




      directionsService.route({
          origin: {placeId: 'ChIJm_7YeFme4jARgJ_Qkq0w9NM' },
          destination: {placeId: 'ChIJz-QtE-6e4jARspPun_tlAqc'},
          waypoints: waypts,
          optimizeWaypoints: false,
          travelMode: 'DRIVING'
        }, function(response, status) {
          if (status === 'OK') {
            directionsDisplay.setDirections(response);
            var route = response.routes[0];
          } else {
            window.alert('Directions request failed due to ' + status);
          }
        });
      }

    </script>
    <script async defer
    src="http://maps.googleapis.com/maps/api/js?key=AIzaSyB70wPQAQR-5P86DJ2j1QcAgYVbR0-xD_k&callback=initMap">
    </script>
  </body>
</html>'''
        self.setHtml(self.html)
