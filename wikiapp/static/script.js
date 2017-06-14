$(document).ready(function(){

    $('#clear').on('click', function() {
      // clears the query string and url
      // resets the search term and jinja variable in app layout

      window.location.href =  window.location.href.split("?")[0]
      $('#query').attr({'placeholder':'Type search term here'})
      $('#output').html('<h2>{{query | safe}}</h2>{{result | safe}}')

    });

})
