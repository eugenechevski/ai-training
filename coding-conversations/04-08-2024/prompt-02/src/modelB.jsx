import React, { useRef, useEffect } from 'react';
import * as d3 from 'd3';

const BarChart = ({ data }) => {
  const svgRef = useRef();

  useEffect(() => {
    // Set up SVG dimensions
    const width = 400;
    const height = 300;
    const svg = d3.select(svgRef.current)
      .attr('width', width)
      .attr('height', height);

    // Set up scales
    const xScale = d3.scaleBand()
      .domain(data.map((d) => d.category))
      .range([0, width])
      .padding(0.2);
    const yScale = d3.scaleLinear()
      .domain([0, d3.max(data, (d) => d.value)])
      .range([height, 0]);

    // Create bars
    svg.selectAll('rect')
      .data(data)
      .join('rect')
      .attr('x', (d) => xScale(d.category))
      .attr('y', (d) => yScale(d.value))
      .attr('width', xScale.bandwidth())
      .attr('height', (d) => height - yScale(d.value))
      .attr('fill', 'steelblue');
  }, [data]);

  return <svg ref={svgRef} />;
};

export default BarChart;