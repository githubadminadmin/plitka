jQuery(document).ready(function ($) {

      $('body').on('change', 'input[type="checkbox"]',function(){
            var sendData = $(this).closest('form').serialize();
            var url = $('form').attr('action');
            
            $.ajax({
                type: "GET",
                url: url,
                data: sendData,
                cache: false,   
                success: function(data){
                    $('#filter').html(data.filter_setting);
                    $('#prod').html(data.product_view);
                    console.log(data.product_view);
                    window.history.pushState({route: data.url}, "EVILEG", data.url)
                    //$('.shopping-cart-table tbody').html(data.cart_body)
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