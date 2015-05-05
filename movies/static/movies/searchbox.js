function search() {
  document.getElementById("search").style.color = "red";
}

function initialize() {
  var myLatlng = new google.maps.LatLng(37.7749295, -122.4194155);
  var mapOptions = {
    zoom: 12,
    center: myLatlng
  }
  var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

  var marker = new google.maps.Marker({
      position: myLatlng,
      map: map,
      title: 'Hello World!'
  });

  var e = document.getElementById("select-input");
  var value = e.options[e.selectedIndex].value;
  console.log(value);
}

google.maps.event.addDomListener(window, 'load', initialize);

