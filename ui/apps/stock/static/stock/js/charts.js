require.config({
  baseUrl: '../../../static',
  paths: {
    'echarts': 'echarts',
    'echarts/theme/dark': 'echarts/theme/dark',
    'underscore': 'underscore/underscore'
  }
});
require(
  [
    'echarts',
    'echarts/theme/dark',
    'echarts/chart/line',   // 按需加载所需图表，如需动态类型切换功能，别忘了同时加载相应图表
    'echarts/chart/bar',
  ],
  function (ec, theme) {
    var myChart = ec.init(document.getElementById('stock-line'), theme);
    var ecConfig = require('echarts/config');
    var option = {
      title : {
        text: 'XX股票分析',
      },
      tooltip : {
        trigger: 'axis'
      },
      legend: {
        data:['价格','情绪指数']
      },
      calculable : true,
      grid: {
        x: 40,
        x2: 40,
      },
      dataZoom : {
          show : true,
          realtime : true,
          start : 0,
          end : 100
      },
      xAxis : [
        {
          type : 'category',
          boundaryGap : false,
          data : [1,2,3,4]
        }
      ],
      yAxis : [
        {
          name: '价格',
          type : 'value',
          axisLabel : {
            formatter: '{value}'
          }
        },
        {
          name: '情绪值',
          type : 'value',
          axisLabel : {
            formatter: '{value}'
          }
        },
      ],
      series : [
        {
          name:'价格',
          type:'line',
          data:[1,2,3,4],
          symbolSize: '1',
          itemStyle: {
            normal: {
              lineStyle: {
                width: '0.8'
              }
            }
          }
        },
        {
          name:'情绪指数',
          type:'line',
          yAxisIndex: 1,
          data:[6100,1200,4002,1992],
          symbolSize: '1',
          itemStyle: {
            normal: {
              lineStyle: {
                width: '0.8'
              }
            }
          }
        }
      ]
    };
    var getChartData = function (instrId) {
      var instrId = instrId || '';
      if (instrId){
        myChart.clear();
      }
      $.getJSON('get_chart_data', {'instrId': instrId}, function (data) {
        option['xAxis'][0]['data']=data['time'];
        option['series'][0]['data']=data['price_value'];
        option['series'][1]['data']=data['instrument_fasi'];
        option['title']['text']=data['instrument']
        myChart.setOption(option);
      });
    }

    var $tpl = $('#tplNews').html();
    var get_news = function (data_time) {
      $.getJSON('get_news', {'time': data_time}, function (data) {
        $("#news-content").html(_.template($tpl, {'data': data}));
        $("#news-accordion").find('.panel-collapse:eq(0)').addClass('in');
      })
    }

    myChart.on(ecConfig.EVENT.CLICK, function (p, o) {
      if (['最小值', '最大值'].indexOf(p.name) === -1) {
        get_news(p.name)
      }
    });

    getChartData($('[name=instr_id]').val());

    $("#full-line-chart").on('shown.bs.modal', function () {
      var fullChart = ec.init(document.getElementById('stock-full-screen'), theme);
      fullChart.setOption(option);
    });
  }
);
