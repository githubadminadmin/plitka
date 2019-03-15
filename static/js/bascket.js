function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

jQuery(document).ready(function ($) {
    $('body').on('submit', '.add_cart', function(e){

        e.preventDefault();
        url = $(this).attr('action')
        var data = $(this).serialize();
        $.ajax({
            type: "POST",
            url: url,
            data: data,
            cache: false,
            success: function(data){
                $('.cart_item').html(data.cart_header)
                $('.shop_table tbody').html(data.cart_body)
                if (data == 'ok'){
                   //location.reload();
                }
                else{
                   $('#error-login').html(data);
                }
            }
       });
    });
    
    $('body').on('click', '.cart_remove', function(e){
        e.preventDefault();
        url = $(this).attr('href')
        $.ajax({
            type: "POST",
            url: url,
            data: {csrfmiddlewaretoken: csrftoken},
            cache: false,
            success: function(data){
                $('.cart_item').html(data.cart_header)
                $('.shop_table tbody').html(data.cart_body)
                if (data == 'ok'){
                   //location.reload();
                }
                else{
                   $('#error-login').html(data);
                }
            }
       });
    });

});