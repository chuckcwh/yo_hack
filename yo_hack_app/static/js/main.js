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

    $('#dash_save').on('click', function() {
        var word1 = $('#id_word1').val();
        var word2 = $('#id_word2').val();
        data = {
            'word1': word1,
            'word2': word2
        };
        $.ajax({
            url: '/save-words/',
            type: 'POST',
            dataType: 'json',
            data: JSON.stringify(data)

        })
    });

    var family_member = $('.family-box').first().html();
    var action;
    $('.family-box').on('click', function(){
        family_member = $(this).html();
    });

    $('.action').on('click', function() {
        action = $(this).attr('id');
        $.ajax({
            url: '/get-action/?sender='+family_member+'&action='+action,
            type: 'GET',
            dataType: 'json',
//            data: JSON.stringify(data),
            success: function(data){
                console.log("returned");
                console.log(data);
                if (action == 0) {
                    hello_display(data);
                } else if (action == 1) {
                    map_display(data, 1);
                } else {
                    map_display(data, 2);
                }
            }
        });

    });

    var count = 0;
    $('.family-box').each(function() {
        if(count < color_list.length){
            count ++;
        }
        else {
            count = 0;
        }
        $(this).css('background-color', color_list[count]);
    });

    function hello_display(data){
        $('#hello_display_window').show();
        $('#map_display_window').hide();
        $('.hello_display').html('');

        for (i = 0; i < data.length; i++){
            $('.hello_display').append('<tr>' +
                '<td>' + data[i].fields.time.split('T')[0] + '</td>' +
                '<td>' + data[i].fields.time.split('T')[1].split('.')[0] + '</td>' +
                '<td>' + data[i].fields.text + '</td>' +
                '<tr>');
            console.log(data[i].fields.text);
        }
    }

    var map;
    var markers = [];
//    var info_windows = [];
    function initialize() {
        var mapOptions = {
          center: { lat: 37.7577, lng: -122.4376},
          zoom: 14
        };
        map = new google.maps.Map(document.getElementById('map-canvas'),
            mapOptions);
      }
      google.maps.event.addDomListener(window, 'load', initialize);

    function map_display(data, type){
        for (var i = 0; i < markers.length; i++) {
                markers[i].setMap(null);
            }
        var kind;
        if (type === 1) {
            kind = "Yo I'm lost."
        }
//        markers = [];
        $('#hello_display_window').hide();
        $('#map_display_window').show();

        console.log(data);
        var lat = parseFloat(data[0].fields.latitude);
        var lon = parseFloat(data[0].fields.longitude);
        console.log(lat);
        console.log(lon);
        var center = map.setCenter(new google.maps.LatLng(lat, lon));
        for (i=0; i<data.length; i++) {
            console.log(data[i].fields.time.split('T')[0]);
            var info_content = "<h3>" + kind + "</h3>" + data[i].fields.time.split('T')[0] + "<br>" + data[i].fields.time.split('T')[1].split('.')[0];
            var infowindow = new google.maps.InfoWindow({
                content: info_content
            });
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(parseFloat(data[i].fields.latitude), parseFloat(data[i].fields.longitude)),
                map: map
            });
            google.maps.event.addListener(marker, 'click', function(){
                infowindow.open(map, marker);
            });
            markers.push(marker);
        }
////        $('#map_display_window').append();
    }

});