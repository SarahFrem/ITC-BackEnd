board_obj = {};

board_obj.displayWrittingBox = function (){

    var loc = $('#writting-box');

    $('<div></div>')
        .appendTo(loc)
        .attr('id', 'text-box');

    $('<input></input>')
        .appendTo($("#text-box"))
        .attr('id', 'title-box')
        .attr('placeholder', 'title')
        .attr('type', 'text')

    $('<input></input>')
        .appendTo($("#text-box"))
        .attr('id', 'message-box')
        .attr('placeholder', 'Your message here')
        .attr('type', 'text')

    $('<input></input>')
        .appendTo($("#text-box"))
        .attr('id', 'author-box')
        .attr('placeholder', 'author')
        .attr('type', 'text')  
};

board_obj.displayButtons = function (){
   $("#btn-check-close").css('display', 'block');

};

board_obj.close = function (){
    $("#writting-box").empty();
    $('#btn-check-close').css('display','none');
    $("#btn-plus").css('display', 'block');
};





board_obj.send_DB = function (){

    var datas = {'title':$('#title-box').val(), "content":$('#message-box').val(), "author":$('#author-box').val()};

    $.ajax({
        type: 'POST',
        url: 'http://localhost:8000/bill/board/datas',
        data: datas,

        success: function(datas){
           console.log(datas)
            board_obj.displayNewMessage(datas['title'], datas['content'], datas['author']);
        },
        error: function(xhr, textStatus, error){
            console.log("error in datas post :");
        }
      });
};


board_obj.displayError = function(){
    //write only a sentence like error please send your message again
};

board_obj.displayNewMessage = function(){

    var datas = {'title':$('#title-box').val(), "content":$('#message-box').val(), "author":$('#author-box').val()};

    var first_div = $('<div></div>');
    first_div.appendTo($('.past-messages'));
    first_div.addClass('row message');

    var second_div = $('<div></div>');
    second_div.appendTo(first_div);
    second_div.addClass('col regular-box');
    second_div.text(new Date());

    var third_div = $('<div></div>');
    third_div.appendTo(first_div);
    third_div.addClass('title-style');
    third_div.text(datas.title);

    var thourth_div = $('<div></div>');
    thourth_div.appendTo(first_div);
    thourth_div.addClass('content-style');
    thourth_div.text(datas.content);

    var fifth_div = $('<div></div>');
    fifth_div.appendTo(first_div);
    fifth_div.addClass('author-style');
    fifth_div.text(datas.author);
};


$(document).ready(function(){
    $("#btn-check-close").css('display', 'none');
   
    $("#plus").on('click', function(){
        $("#btn-plus").css('display', 'none');
        board_obj.displayWrittingBox();
        board_obj.displayButtons();
    });

    $("#close").on('click', function(){
        board_obj.close();
    });

    $("#check").on('click', function(){
        board_obj.displayNewMessage();
        board_obj.close();
        board_obj.send_DB();
    });
});



