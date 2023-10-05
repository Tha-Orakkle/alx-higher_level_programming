$('document').ready(function () {
  $('input#language_code').focus(function () {
    $(this).keydown(function (event) {
      if (event.keyCode === 13) {
        $('input#btn_translate').click();
      }
    });
  });

  $('input#btn_translate').on('click', function () {
    const url = 'https://hellosalut.stefanbohacek.dev/?';
    //   const url = 'https://www.fourtonfish.com/hellosalut/?';
    const languageCode = $('input#language_code').val();
    $.get(url + $.param({ lang: languageCode }), function (data) {
      $('div#hello').text(data.hello);
    });
  });
});
