var bill = {};



$( document ).ready(function() {
    $('#login').attr('href', 'login');
    $('#register').attr('href', 'registration');

    $('#login').on('click', function(){
        console.log('ok for login');
    });

    $('#register').on('click', function(){
        console.log('ok for reg');
    });

});