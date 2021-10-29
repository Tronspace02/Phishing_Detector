function triggerEmpty(){
      $("h3").empty()
      $("p").empty()
}

$("#testUrl").on("click", function(){
    $( ".progressBar").animate({height:"toggle"}, function() {
        // Animation complete.
        $(this).fadeIn();
      });
    triggerEmpty();
});

$("#reset").on("click",function(){
    $( "#displayEle").animate({height:"toggle"}, function() {
        // Animation complete.
        triggerEmpty();
        $("form").trigger("reset");
        window.location.href='http://127.0.0.1:5000/';
      });
});
