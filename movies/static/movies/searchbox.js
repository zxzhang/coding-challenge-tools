var markers = [];
var comments = [];
var mapOptions = {};
var infowindow;
var map;
var myLatlng;

function search() {
  var search = document.getElementById("search");
  var url = search.attributes.href.nodeValue;
  var content = document.getElementById("select-input").value;
  var term = document.getElementById("pac-input").value;
  var csrf = document.getElementsByName("csrfmiddlewaretoken");
  // using ajax to get the search result and draw the marker on the map
  $.ajax({
    type: "POST",
    url: url,
    data: {
      content: content,
      term: term,
      csrfmiddlewaretoken: csrf[0].value
    },
    success: search_success,
    dataType: 'html'
  });
}

function search_success(data, textStatus, jqXHR){
    // parse the xml data and update the marker and infowindow
    var places = [];
    comments = [];
    var xmlDoc = $.parseXML(data);
    var data = xmlDoc.documentElement.childNodes;
    for (var i = 0; i < data.length; i++) {
      if (data[i].nodeType === 1) {
        var nodes = data[i].childNodes;
        var place = new Object();
        var contentString = ""; 
        for (var j = 0; j < nodes.length; j++) {
          if (nodes[j].nodeType === 1) {
            if (nodes[j].nodeName === "title") {
              place.title = nodes[j].textContent;
              contentString += '<h1>' + nodes[j].nodeName + '</h1>';
               contentString += '<p>' + nodes[j].textContent + '</p>';
            } else if (nodes[j].nodeName === "lat") {
              place.lat = Number(nodes[j].textContent);
            } else if (nodes[j].nodeName === "lng") {
              place.lng = Number(nodes[j].textContent);
            } else if (nodes[j].nodeName.length > 0 && nodes[j].textContent.length > 0) {
              contentString += '<h1>' + nodes[j].nodeName + '</h1>';
              contentString += '<p>' + nodes[j].textContent + '</p>';
            }
          }
        }
        places.push(place);  
        comments.push(contentString);
      }
    }

  if (places.length == 0) {
    return;
  }
  for (var i = 0, marker; marker = markers[i]; i++) {
    marker.setMap(null);
  }
  markers = [];
  var bounds = new google.maps.LatLngBounds();

  for (var i = 0, place; place = places[i]; i++) {
    var latLng = new google.maps.LatLng(place.lat, place.lng);

    // update the marker
    var marker = new google.maps.Marker({
      map: map,
      title: place.title,
      position: latLng
    });

    google.maps.event.addListener(marker, 'click', function() {
      // update the info window
      var pos = markers.indexOf(this);
      infowindow.setContent(comments[pos]);
      infowindow.open(map, this);
    });
    markers.push(marker);
    bounds.extend(latLng);
  }
  map.fitBounds(bounds);
}

function initialize() {
  myLatlng = new google.maps.LatLng(37.7749295, -122.4194155);
  infowindow = new google.maps.InfoWindow({
      content: ""
  });

  mapOptions = {
    zoom: 12,
    center: myLatlng
  }
  map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
}

google.maps.event.addDomListener(window, 'load', initialize);

