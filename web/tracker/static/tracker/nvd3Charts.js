function lineChart(id, data) {
    nv.addGraph(function() {
        var chart = nv.models.lineChart()
            .margin({left: 40, right: 40})
            .showLegend(false)
            .forceY(0)
            .forceY(2)
        ;
        chart.xAxis
            .tickFormat(function(d) {
                return d3.time.format('%Y-%m-%d')(new Date(d));
            })
        ;
        chart.yAxis
            .showMaxMin(false)
            .tickFormat(d3.format('.1f'))
        ;
        d3.select(id)
            .datum(data)
            .call(chart)
        ;
        nv.utils.windowResize(chart.update);
        return chart;
    });
}

function durationChart(id, data, tickFormatter) {
    nv.addGraph(function() {
        var chart = nv.models.linePlusBarChart()
            .color(['#e67b00'])
            .margin({left: 40, right: 40, top:10, bottom: 25})
            .x(function(d, i) { return i })
            .y(function(d, i) { return d[1] })
            .showLegend(false)
            .interpolate('step-after')
        ;
        chart.xAxis
            .tickFormat(function(x) {
                return tickFormatter(data[0].values[x]);
            })
        ;
        chart.y1Axis
            .tickFormat(d3.format('.1f'))
            .showMaxMin(false)
        ;
        chart.bars
            .forceY([0])
        ;
        chart.y2Axis
            .tickFormat(d3.format('.1f'))
            .showMaxMin(false)
        ;
        chart.lines
            .forceY([0])
        ;
        d3.select(id)
            .datum(data)
            .transition()
            .duration(0)
            .call(chart)
        ;
        nv.utils.windowResize(chart.update);
        return chart;
    });
}
