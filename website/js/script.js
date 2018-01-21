function calculatDuration(directionsService, origin, destination, callback){
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

function getClosestBarrack(directionsService, latLng, callback) {
    $.getJSON("casernes.geojson", function(data){
        var min_duration;
        var closest_barrack;
        var barracks = data["features"];
        for (b in barracks){
            var barrack_position = barracks[b]["geometry"]["coordinates"];
            var barrack_latlng = new google.maps.LatLng({lat: barrack_position[1], lng: barrack_position[0]});
            calculatDuration(directionsService, barrack_latlng, latLng, function(result){
                var duration = result["duration"];
                if(!min_duration | duration < min_duration){
                    min_duration = duration;
                    // closest_barrack is not assigned correctly
                    closest_barrack = result["origin"];
                }
            });
        }
        console.log(closest_barrack);
        callback(closest_barrack);
    });
}

function initMap() {
    var montreal = {lat: 45.5052846, lng: -73.6116984};
    var directionsService = new google.maps.DirectionsService;
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

    // images
    var fire_image = 'images/fire.png';
    var firemen_image = 'images/firemen.png';

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

    // Fire icons on click
    map.addListener('click', function(event) {
        var fire_position = event.latLng;
        var marker = new google.maps.Marker({
            position: fire_position,
            icon: fire_image,
            map: map
        });
        getClosestBarrack(directionsService, event.latLng, function(closest_barrack){
            console.log(closest_barrack);
        });
        marker.addListener('click', function(){
            marker.setMap(null);
        });
    });

}

