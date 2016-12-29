var source = new EventSource("subscribe");

var statusBoard = document.getElementById('status-board');
var imgList = document.getElementById('imgList');

var count = 0;

source.onmessage = function(e) {
    if (count == 0) {
         count = e.data;
    } else {
        if (e.data > count) {
            updateBoard(count)
        };
        count = e.data;
    };
};


function updateBoard(d){

    $.ajax({
        url: "/api/imgboard",
        dataType: "json",
        success: function(result) {
            $.each(result.result, function(key,value){
                $("#imgList").prepend("<span class='thumb-wrap'><a href='"+value.image+"'><img src='"+value.thumb+"'></span>");
            });
        }
    });
};
