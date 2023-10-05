$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (movies) {
      $.each(movies.results, function (i, movie) {
        const title = '<li>' + movie.title + '</li>';
        $('ul#list_movies').append(title);
        // console.log(movie.title);
      });
    }
  });
});
