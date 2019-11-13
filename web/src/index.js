const d3 = Object.assign({}, require('d3'), require('d3-tube-map'));
const data = require('./pubs.json');

const container = d3.select('#tube-map');

const width = 1000;
const height = 500;

const map = d3
  .tubeMap()
  .width(width)
  .height(height)
  .margin({
    top: 20,
    right: 20,
    bottom: 40,
    left: 100,
  })
  .on('click', name => {
    console.log(data.stations[name]);
  });

container.datum(data).call(map);
