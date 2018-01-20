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
    map.addListener('click', function(event) {
        var fire_position = event.latLng;
        var image = 'images/fire.png';
        var marker = new google.maps.Marker({
            position: fire_position,
            icon: image,
            map: map
        });
    });
}
