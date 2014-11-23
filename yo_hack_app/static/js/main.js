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
        data['name_list']=name_list;
        console.log(data);
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

    function emergency_callback(userLat, userLon) {
        data = {
//            'text': $('#hello_text').val(),
            'userLat': userLat,
            'userLon': userLon
        };
        ajax_call('/emergency/', data);
    }

    function lost_callback(userLat, userLon) {
        data = {
//            'text': $('#hello_text').val(),
            'userLat': userLat,
            'userLon': userLon
        };
        ajax_call('/im-lost/', data);
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

    $('#lost').on('click', function() {
        get_location(lost_callback);
    });

    $('.word').on('click', function(){
        data = {
            'text': $(this).text()
        };
        ajax_call('/hello/', data)
    });

    var name_list = [];
    var color_list = ['#1ABC9C', '#3498DB', '#34495E', '#8E44AD', '#9B59B6'];
    $('.name_click').on('click', function(){
        name_tag = $(this).text();
        name_list.push(name_tag);
        console.log(name_list);
    });

    var count = -1;
    $('.name_click').each(function() {
        if(count < color_list.length){
            count ++;
        }
        else {
            count = 0;
        }
        $(this).css('background-color', color_list[count]);
    });

    $('#go_action, #dashboard_action').on('click', function () {
        window.location.href = "/action/";
    });
    $('#go_dashboard, #action_dashboard').on('click', function () {
        window.location.href = "/dashboard/";
    });
    $('#go_logout').on('click', function () {
        window.location.href = "/logout/";
    });
    $('#go_login').on('click', function () {
        window.location.href = "/login/";
    });
    $('#go_register').on('click', function () {
        window.location.href = "/register/";
    });

//    $('#dash_save').on('click', function() {
//        var word1 =
//    })

});