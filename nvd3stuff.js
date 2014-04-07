d3.json('weightdata.json', function(json) {
    nv.addGraph(function() {
        var chart = nv.models.lineWithFocusChart();
        var varb = [json[0], json[1]].map(function(json, i) {
            return {
                key: json.name,
                values: json.data
            };
        });

        chart.margin({left: 80 });
        chart.xAxis.tickFormat(function(d) {
            return d3.time.format('%d-%m-%y')(new Date(d * 1000));
        })
        chart.yAxis.axisLabel('weight [kg]').tickFormat(d3.format(',.2f'));

        chart.x2Axis.axisLabel('date').tickFormat(function(d) {
            return d3.time.format('%d-%m-%y')(new Date(d * 1000));
        })

        chart.y2Axis.tickFormat(d3.format(',.2f'));

        chart.tooltipContent(function(key, y, e, graph) {
            return '<p>' + y + '</p>' + '<p>' + e + '</p>'
        })


        d3.select('#chart svg').datum(varb).transition().duration(500).call(chart);
        nv.utils.windowResize(chart.update);
        return chart;
    });
});
