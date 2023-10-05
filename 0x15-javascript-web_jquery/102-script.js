$('document').ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?';
  //   const url = 'https://www.fourtonfish.com/hellosalut/?';

  $('input#btn_translate').click(function () {
    const languageCode = $('INPUT#language_code').val();
    $.get(url + $.param({ lang: languageCode }), function (data) {
      $('div#hello').text(data.hello);
    });
  });
});
