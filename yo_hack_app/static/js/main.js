$(document).ready(function() {

    $('#hello').on('click', function(){
        data = {
            'text': $('#hello_text').val()
        };
        console.log('hello action');
        $.ajax({
            url: '/hello/',
            type: 'POST',
            dataType: 'json',
            data: JSON.stringify(data),
            success: function(data) {
                console.log("successfully returned!");
                console.log(data);
            }
        });
    });

    $('#help').on('click', function(){
        data = "ya";
        $.ajax({
            url: '/help/',
            type: 'POST',
            dataType: 'json',
            data: JSON.stringify(data),
            success: function(data) {
                console.log("successfully returned!");
                console.log(data);
            }
        });
    });


});