$(function () {
  const hdr = $('header');

  $('div#toggle_header').click(function () {
    if (hdr.hasClass('green')) {
      hdr.removeClass('green');
      hdr.addClass('red');
    } else {
      hdr.removeClass('red');
      hdr.addClass('green');
    }
  });
});
