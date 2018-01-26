function myAl(){
     alert("we don't actually serve pizza...");
}

$(document).ready(function(){
    alert("hello!");

    $('#red').click(myAl);

    $('#blue').click(function(){
        alert("we don't actually serve pizza...");
    });

    $('#orange').click(function(){
        alert("we don't actually serve pizza...");
    });

    $('#purple').click(function(){
        alert("we don't actually serve pizza...");
    });

});
