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
    var myChart = ec.init(document.getElementById('hot-chart'), theme);
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
          data:[9,7,8],
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
    myChart.setOption(option);
    var render = function () {
      var $fatherDiv = $('#hot-chart')
      var width = $fatherDiv.width(),
        height = $fatherDiv.height();

      var color = d3.scale.category20c();

      var treemap = d3.layout.treemap()
        .size([width, height])
        .padding(4)
        .value(function(d) { return d.size; });

      var div = d3.select("#hot-chart").append("div")
        .style("position", "relative")
        .style("width", width + "px")
        .style("height", height + "px");
        d3.json("../static/choice/flare.json", function(error, root) {
          div.selectAll(".node")
          .data(treemap.nodes(root))
          .enter().append("div")
          .attr("class", "node")
          .style("left", function(d) { return d.x + "px"; })
          .style("top", function(d) { return d.y + "px"; })
          .style("width", function(d) { return Math.max(0, d.dx - 1) + "px"; })
          .style("height", function(d) { return Math.max(0, d.dy - 1) + "px"; })
          .style("line-height", function (d) {return Math.max(0, d.dy - 1) + "px";})
          .style("background", function(d) { return d.children ? color(d.name) : null; })
          .style("cursor", "pointer")
          .text(function(d) { return d.children ? null : d.name; });
        });
    };


    $.getJSON('get_choice_list', function (data) {
      $('#stock-list').html(_.template($('#tpl-stcok').html(), {data: data}));

      $('.topnav').find('a').on('click', function () {
        if ($(this).find('span').length === 1){
          var strall = $(this).text();
          var nav_status = strall.slice(-3);
          if (nav_status === '[+]') {
            var nav_name = strall.slice(0, -3);
          }
        }
        if ($(this).parent().attr('class') === 'exchange-name') {
          var exchangeName = $(this).text().slice(0,-3);
          $.getJSON('change_hot_chart', {'name': exchangeName}, function () {
          });
          //myChart.dispose();
          $('#hot-chart').empty();
          render();

          $('#hot-chart div').on('click', function (e) {
            $src = $(e.target);
            instrName = $src.text();
            $.getJSON('hot_to_chart', {'name': instrName}, function (data) {
              window.location.href = '/stock/?in_id=' + data.id;
            });
          });
        }
      });

      $(".topnav").accordion({
        accordion:false,
        speed: 500,
        closedSign: '[+]',
        openedSign: '[-]'
      });


      $('.instrument-name').on('click', function (e) {
        var instrName = $(this).find('a').text().slice(0,-4);
        var $src = $(e.target);
        if ($src.context.localName === 'a') {
          $.getJSON('/stock/get_chart_data', {'instr_name': instrName}, function (data) {
            option['xAxis'][0]['data']=data['time'];
            option['series'][0]['data']=data['price_value'];
            option['series'][1]['data']=data['instrument_fasi'];
            option['title']['text']=data['instrument']
            var myChart = ec.init(document.getElementById('hot-chart'), theme);
            myChart.setOption(option);
          });
          $('#hot-chart').empty();
          var myChart = ec.init(document.getElementById('hot-chart'), theme);
          myChart.setOption(option);
        }
        else {
          var dataName = $src.parent().text().slice(0,-4);
          $('#watchlist').attr('data-name', dataName);
        }
      });
    })
  }
);
