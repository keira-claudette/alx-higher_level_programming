$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (index, value) {
    $('<li>' + value.title + '</li>').appendTo('ul#list_movies');
  });
});
