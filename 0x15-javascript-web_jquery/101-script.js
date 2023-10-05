window.onload = function () {
  const parent = $('.my_list');

  console.log(parent);

  $('div#add_item').click(function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    parent.append(newItem);
  });
  $('div#remove_item').click(function () {
    $('ul.my_list li:last-child').remove();
  });

  $('div#clear_list').click(function () {
    parent.empty();
  });
};
