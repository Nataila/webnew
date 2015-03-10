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
          data : []
        }
      ],
      yAxis : [
        {
          type : 'value',
          axisLabel : {
            formatter: '{value}'
          }
        }
      ],
      series : [
        {
          name:'价格',
          type:'line',
          data:[],
          markPoint : {
            data : [
              {type : 'max', name: '最大值'},
              {type : 'min', name: '最小值'}
            ]
          },
          markLine : {
            data : [
              {type : 'average', name: '平均值'}
            ]
          }
        },
        {
          name:'情绪指数',
          type:'line',
          data:[],
          markPoint : {
            data : [
              {type : 'max', name: '最大值'},
              {type : 'min', name: '最小值'}
            ]
          },
          markLine : {
            data : [
              {type : 'average', name: '平均值'}
            ]
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

    getChartData($('[name=instr_id]').val());

    //$('.instrument-name a').on('click', function () {
    //  var instrId = $(this).data('id');
    //  getChartData(instrId);
    //})

    $("#full-line-chart").on('shown.bs.modal', function () {
      var fullChart = ec.init(document.getElementById('stock-full-screen'), theme);
      fullChart.setOption(option);
    });

  }
);
