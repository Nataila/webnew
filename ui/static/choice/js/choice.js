$(document).ready(function () {

  $('.watch-list-ok').on('click', function () {
    var id = $('#watch-select').val();
    var instrName = $('#watchlist').data('name');
    $.getJSON('/stock/add_to_list', {'to_list': id, 'instr_name': instrName}, function (data) {
      if (data.code === 200) {
        window.location.href = '/stock?in_id=' + data.instr_id;
      }
      else {
        $('.instr_error').text(data.msg)
      }
    })
  });

  // choice页面筛选
  $('#choice-search').keydown(function (e) {
    if (e.keyCode === 13) {
      var search_type = $(this).val();
      if (isNaN(search_type)) {
        var s_data = search_type;
      }
      else {
        var s_data;
        $.ajax({
          method: 'get',
          url: 'code_to_name',
          data: {'code': search_type},
          async: false,
          success: function (data) {
            s_data = data;
          }
        })
      }
      $('.country ul').css('display', 'none');
      $('.instrument-name a').each(function (i, j) {
        var content = $(j).text().slice(0, -4);
        if (content === s_data){
          $(this).closest('.country').find('.country-a').trigger('click');
          $(this).closest('.exchange-name').find('.exchange-a').trigger('click');
          $(this).closest('.indu-name').find('.indu-a').trigger('click');
          $(this).addClass('search_done');
        }
      })
    }
  });

})
