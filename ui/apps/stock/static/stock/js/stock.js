$(document).ready(function () {
  $('#exchange').find('.panel-collapse:eq(0)').addClass('in');
  var $tpl = $('#tplNews').html();
  var get_news = function (instrId) {
    $.getJSON('get_news', {'instrId': instrId}, function (data) {
      $("#news-content").html(_.template($tpl, {'data': data}));
      $("#news-accordion").find('.panel-collapse:eq(0)').addClass('in');
    })
  }

  $('.remove').on('click', function () {
    $.getJSON('remove_watch', {'instrname': $(this).prev().text()}, function (data) {
      if (data.code === 200) {
        window.location.reload();
      }
    })
  })
  var instrId = $('[name=instr_id]').val();
  get_news(instrId);
  $('#test').on('click', function () {
    get_news(1);
  })
})
