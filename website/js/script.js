function getDuration(directionsService, origin, destination, callback){
    directionsService.route({
        origin: origin,
        destination: destination,
        travelMode: 'DRIVING'
    }, function(response, status){
        if(status === 'OK'){
            var totalDuration = 0;
            var legs = response.routes[0].legs;
            for(var i=0; i<legs.length; ++i) {
                totalDuration += legs[i].duration.value;
            }
            var result = {origin: origin, duration: totalDuration};
            callback(result);
        }
        else{
            throw status;
        }
    });
}

async function getDurations(barracks, latLng, directionsService, callback){
    var durations = [];
    barracks.forEach(function(barrack, b, array){
        var barrack_position = barrack["geometry"]["coordinates"];
        var barrack_latlng = new google.maps.LatLng({lat: barrack_position[1], lng: barrack_position[0]});
        getDuration(directionsService, barrack_latlng, latLng, function(result){
            durations.push(result);
            // Ugly way to do the proper callback to populate correctly durations array and callback on it
            if (durations.length === array.length){
                callback(durations);
            }
        });
    });
}

function getMinDurationObject(durations){
    var min_result = {duration: Infinity};
    durations.forEach(function(item, i){
        if (item["duration"] < min_result["duration"]){
            min_result = item;
        }
    });
    return min_result;
}

function getClosestBarrack(directionsService, latLng, callback) {
    $.getJSON("casernes.geojson", function(data){
        var barracks = data["features"];
        getDurations(barracks, latLng, directionsService, function(durations){
            closest_barrack = getMinDurationObject(durations);
            callback(closest_barrack["origin"]);
        });
    });
}

function initMap() {
    var montreal = {lat: 45.5052846, lng: -73.6116984};
    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 15,
        center: montreal,
        styles: [
            {
                featureType: "poi",
                stylers: [
                    { visibility: "off" }
                ]
            },
            {
                featureType: "poi.park",
                stylers: [
                    { visibility: "on" }
                ]
            },
            {
                featureType: "poi.government",
                stylers: [
                    { visibility: "on" }
                ]
            },
            {
                featureType: "poi.school",
                stylers: [
                    { visibility: "on" }
                ]
            },

        ]
    });


    directionsDisplay.setMap(map);

    // images
    var fire_image = 'images/fire.png';
    var firemen_image = 'images/firemen.png';
    var green_light_image = 'images/green_light.png';

    // Barracks icons
    $.getJSON("casernes.geojson", function(data){
        var barracks = data["features"];
        for (b in barracks){
            var barrack_position = barracks[b]["geometry"]["coordinates"];
            var barrack_latlng = new google.maps.LatLng({lat: barrack_position[1], lng: barrack_position[0]});
            new google.maps.Marker({
                position: barrack_latlng,
                icon: firemen_image,
                map: map
            });
        }
    });

    var light_marker;

    $.getJSON("geo_redlights.json", function(data){
        var traffic_lights = data["features"];
        for (b in traffic_lights){
            var traffic_lights_position = traffic_lights[b]["geometry"]["coordinates"];
            var traffic_lights_latlng = new google.maps.LatLng({lat: traffic_lights_position[0], lng: traffic_lights_position[1]});
            var light_marker = new google.maps.Marker({
                position: traffic_lights_latlng,
                icon: green_light_image,
                map: map
            });
        }
    });

//minFTZoomLevel = 17 ;

//      google.maps.event.addListener(map, 'zoom_changed', function() {
//          var zoom = map.getZoom();

          // Update May 2017
          //   You can now use setVisible() on a marker instead of
          //   setting the map to a null value.
//          if (zoom >= 17) {
//              light_marker.setVisible(false);
//          } else {
//              light_marker.setVisible(true);
//          }
//      });

    // Fire icons on click
    map.addListener('click', function(event) {
        var fire_position = event.latLng;
        var marker = new google.maps.Marker({
            position: fire_position,
            icon: fire_image,
            map: map
        });
        getClosestBarrack(directionsService, fire_position, function(closest_barrack){
            directionsService.route({
                origin: closest_barrack,
                destination: fire_position,
                travelMode: 'DRIVING'
            }, function(response, status) {
                if (status === 'OK') {
                    console.log(response);
                    directionsDisplay.setDirections(response);
                } else {
                    window.alert('Directions request failed due to ' + status);
                }
            });
        });
        marker.addListener('click', function(){
            marker.setMap(null);
        });
    });

}
