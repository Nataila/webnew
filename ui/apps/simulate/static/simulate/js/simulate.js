$(document).ready(function () {
  $('.result').hide();
  $('.btn-start').on('click', function () {
    var send_data = {};
    var data_list = ['instr-code', 'start-time', 'end-time', 'kind', 'right-name', 'left-name']
    $.each(data_list, function (i, j) {
      send_data[j] = $('#'+j).val();
    })
    $.getJSON('get_result', send_data, function (data) {
      console.log(data)
      $('.result').show();
      $('.tactics-cond, .trading-record').css('display', 'block');
    })
  })
})
