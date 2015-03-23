$(document).ready(function () {
  $('.list-content li').on('click', function () {
    console.log(123);
    //$(this).parent().find('li').removeClass();
    $(this).toggleClass('li-selected');
  })

  $('.news-add-ok').on('click', function () {
    var send_data = {
      'source': [],
      'entity': [],
      'incident': []
    };
    var list_id = $('.watch_list').val();
    $.each(send_data, function (i) {
      $('.'+i).find('.li-selected').each(function () {
        send_data[i].push($(this).text());
      });
    });

    $.getJSON('set_news_watch', {'data': JSON.stringify(send_data), 'list_id': list_id}, function (data) {
      var next_path = window.location.pathname + '?list_id' + data.list_id;
      window.location.href = next_path;
    });
  })

})
