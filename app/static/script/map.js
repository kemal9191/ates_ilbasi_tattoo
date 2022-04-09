function initMap() {
    var dumbo = {lat: 40.700802, lng:73.987602};
    var mapOptions = {
        center: dumbo,
        zoom: 10
    };
    var googlemap = new google.maps.Map(document.getElementById("map"), mapOptions);
}

var googlemap = new google.maps.Map(document.getElementById("map"), mapOptions);
            var marker = new google.maps.Marker({
                position: siliconValley,
                map: googlemap
            });