// press enter click the search button
$(document).ready(function(){
    $( '#pac-input' ).keypress(function(e){
      if( e.keyCode === 13 ) {
      	$( '#search' ).click();
      }
    });
});