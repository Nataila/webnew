$(document).ready(function () {
//var render = function () {
//  var $fatherDiv = $('#hot-chart')
//  var width = $fatherDiv.width(),
//    height = $fatherDiv.height();
//
//  var color = d3.scale.category20c();
//
//  var treemap = d3.layout.treemap()
//    .size([width, height])
//    .padding(4)
//    .value(function(d) { return d.size; });
//
//  var div = d3.select("#hot-chart").append("div")
//    .style("position", "relative")
//    .style("width", width + "px")
//    .style("height", height + "px");
//    d3.json("../static/choice/flare.json", function(error, root) {
//      div.selectAll(".node")
//        .data(treemap.nodes(root))
//      .enter().append("div")
//        .attr("class", "node")
//        .style("left", function(d) { return d.x + "px"; })
//        .style("top", function(d) { return d.y + "px"; })
//        .style("width", function(d) { return Math.max(0, d.dx - 1) + "px"; })
//        .style("height", function(d) { return Math.max(0, d.dy - 1) + "px"; })
//        .style("background", function(d) { return d.children ? color(d.name) : null; })
//        .text(function(d) { return d.children ? null : d.name; });
//    });
//
//      $('#hot-chart div').on('click', function (e) {
//        $src = $(e.target);
//        console.log($src.text());
//      })
//  }

 // $('.topnav').find('a').on('click', function () {
 //   if ($(this).find('span').length === 1){
 //     var strall = $(this).text();
 //     var nav_status = strall.slice(-3);
 //     if (nav_status === '[+]') {
 //       var nav_name = strall.slice(0, -3);
 //     }
 //   }
 //   if ($(this).parent().attr('class') === 'exchange-name') {
 //     $('#hot-chart').empty();
 //     render();
 //   }
 // })
})
