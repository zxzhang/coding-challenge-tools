$(function() {
	$( "#pac-input" ).autocomplete({
		source: function( request, response ) {
			var select = document.getElementById("select-input");
			var url = select.options[select.selectedIndex].attributes.href.nodeValue;
			var csrf = document.getElementsByName("csrfmiddlewaretoken");
			$.ajax({
				type: "POST",
				url: url, 
				dataType: "json",
				data: {
					term: request.term,
					csrfmiddlewaretoken: csrf[0].value
				},
				success: function( data ) {
					response( data );
				}
			});
		},
		minLength: 1,
	});
});
