$(document).ready(function() {

    function get_location(callback){
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function (position) {
                var initialLocation = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
                userLat = initialLocation.k;
                userLon = initialLocation.B;
                callback(userLat, userLon);
            });
        }
    }
    function ajax_call(endPoint, data){
        $.ajax({
            url: endPoint,
            type: 'POST',
            dataType: 'json',
            data: JSON.stringify(data),
            success: function(data) {
                console.log("successfully returned!");
                console.log(data);
            }
        });
    }
    $('#hello').on('click', function(){
        data = {
            'text': $('#hello_text').val()
        };
        ajax_call('/hello/', data);

    });

    $('#emergency').on('click', function(){
        get_location(emergency_callback);
    });



    function emergency_callback(userLat, userLon) {
        data = {
            'text': $('#hello_text').val(),
            'userLat': userLat,
            'userLon': userLon
        };
        ajax_call('/emergency/', data);
    }



});