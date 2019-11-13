const d3 = require('d3');
const tubeMap = require('d3-tube-map');
const data = require('./pubs.json');
d3.tubeMap = tubeMap.tubeMap;

const container = d3.select('#tube-map');

const map = d3
  .tubeMap()
  .width(500)
  .height(600)
  .margin({
    top: 0,
    right: 0,
    bottom: 0,
    left: 0,
  })
  .on('click', name => {
    console.log(data.stations[name]);
  });

container.datum(data).call(map);

const svg = container.select('svg');
const zoom = d3
  .zoom()
  .scaleExtent([0.2, 2])
  .on('zoom', () => {
    svg.select('g').attr('transform', d3.event.transform.toString());
  });
const zoomContainer = svg.call(zoom);
const initialScale = 1.2;
const initialTranslate = [0, -20];
zoom.scaleTo(zoomContainer, initialScale);
zoom.translateTo(zoomContainer, initialTranslate[0], initialTranslate[1]);
