d3.json('weightdata.json', function(json) {
    nv.addGraph(function() {
        var chart = nv.models.lineWithFocusChart();
        var varb = [json[0], json[1]].map(function(json, i) {
            return {
                key: json.name,
                values: json.data
            };
        });
        chart.xAxis.tickFormat(function(d) {
            return d3.time.format('%y-%m-%d')(new Date(d * 1000));
        })
        chart.yAxis.tickFormat(d3.format(',.2f'));
        chart.x2Axis.tickFormat(function(d) {
            return d3.time.format('%y-%m-%d')(new Date(d * 1000));
        })
        chart.y2Axis.tickFormat(d3.format(',.2f'));
        d3.select('#chart svg').datum(varb).transition().duration(500).call(chart);
        nv.utils.windowResize(chart.update);
        return chart;
    });
});
