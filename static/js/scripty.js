$(document).ready(function(){
    console.log("loaded");
    $.material.init();

    $(document).on("submit", "#register-form", function(e){
        e.preventDefault();
        var form = $('#register-form').serialize();
        $.ajax({
            url: '/postregistration',
            type: 'POST',
            data: form,
            success: function (response){
                console.log(response);
            }
            });
    });
    console.log("si llega antes")
    $(document).on('submit', '#login-form',function (e){
        e.preventDefault();

        var form = $(this).serialize();
        $.ajax({
            url: '/check-login',
            type: 'POST',
            data: form,
            success: function (res){
                if(res == "error"){
                    alert("coudnt log in.");
                }else {
                    console.log("logged in as", res);
                }
            }
        })
    })
});