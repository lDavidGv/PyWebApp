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
    $(document).on("submit", "#login-form", function (e){
        e.preventDefault();

        var form = $(this).serialize();
        $.ajax({
            url: '/check-login',
            type: 'POST',
            data: form,
            success: function (res){
                if(res === "error"){
                    alert("coudnt log in.");
                }else {
                    console.log("logged in as", res);
                    window.location.href = "/";
                }
            }
        });
    });
    $(document).on("click", "#logout-link", function (e){
        e.preventDefault();

        $.ajax({
            url: '/logout',
            type: 'GET',
            success: function (res){
                if (res === 'success'){
                    window.location.href = '/login';
                }else {
                    alert("something went wrong");
                }
            }
        });
    });
    $(document).on('submit','#post-activity', function (e) {
        e.preventDefault()
        form = $(this).serialize()

        $.ajax({
            url: 'post-activity',
            type: 'POST',
            data: form,
            success: function (res) {
                console.log(res)
            }
    });

    });
    $("#menu-toggle").click(function(e) {
      e.preventDefault();
      $("#wrapper").toggleClass("toggled");
    });
});