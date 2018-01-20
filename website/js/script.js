function initMap() {
    var montreal = {lat: 45.5052846, lng: -73.6116984};
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
        marker.addListener('click', function(){
            marker.setMap(null);
        });
    });

}

