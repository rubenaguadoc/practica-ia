/* eslint-disable no-new */
import { MDCCheckbox } from '@material/checkbox';
import { MDCDrawer } from '@material/drawer';
import { MDCFormField } from '@material/form-field';
import { MDCLinearProgress } from '@material/linear-progress';
import { MDCRipple } from '@material/ripple';
import { MDCSelect } from '@material/select';
import { MDCSnackbar } from '@material/snackbar';
import { MDCTextField } from '@material/textfield';
import { MDCTextFieldIcon } from '@material/textfield/icon';
import { MDCTopAppBar } from '@material/top-app-bar';
// import 'babel-polyfill';

if ('serviceWorker' in navigator) {
  const swName = '../sw.js';
  navigator.serviceWorker.register(swName, { scope: '/' }).catch(console.error);
}

const d3 = require('d3');
const tubeMap = require('d3-tube-map');
const data = require('../data/stations.json');
d3.tubeMap = tubeMap.tubeMap;

new MDCTextField(document.querySelector('.mdc-text-field'));
new MDCTextFieldIcon(document.querySelector('.mdc-text-field__icon'));
new MDCRipple(document.querySelector('.mdc-button'));
const checkbox = new MDCCheckbox(document.querySelector('.mdc-checkbox'));
const formField = new MDCFormField(document.querySelector('.mdc-form-field'));
const topAppBar = MDCTopAppBar.attachTo(document.getElementById('app-bar'));
const drawer = MDCDrawer.attachTo(document.querySelector('.mdc-drawer'));
const snackbar = new MDCSnackbar(document.querySelector('.mdc-snackbar'));
const progress = new MDCLinearProgress(
  document.querySelector('.mdc-linear-progress')
);
progress.close();
formField.input = checkbox;
topAppBar.setScrollTarget(document.getElementById('main-content'));
topAppBar.listen('MDCTopAppBar:nav', () => {
  drawer.open = !drawer.open;
});
const selects = [];
document.querySelectorAll('.mdc-select').forEach(el => {
  selects.push(new MDCSelect(el));
});

let lastSet = 1;

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
    let select;
    if (
      (selects[0].selectedIndex <= 0 || selects[1].selectedIndex > 0) &&
      lastSet !== 0
    ) {
      select = selects[0];
      lastSet = 0;
    } else {
      select = selects[1];
      lastSet = 1;
    }
    select.value = String(data.stations[name].id);
    select.valid = true;
    select.foundation_.notchOutline(true);
    select.label_.float(true);

    Array.from(document.querySelectorAll('tspan')).forEach(el => {
      if (el.innerHTML === name) {
        el.style.fontWeight = 'bolder';
      } else if (lastSet !== 1) {
        el.style.fontWeight = 'normal';
      }
    });

    if (lastSet === 1) {
      triggerSearch();
    }
  });

container.datum(data).call(map);
const svg = container.select('#tube-map > svg');

const zoom = d3
  .zoom()
  .scaleExtent([0.5, 4])
  // .translateExtent([-100, -100], [100, 100])
  .on('zoom', () => {
    if (window.innerWidth < 700) {
      svg.select('g').attr('transform', d3.event.transform.toString());
    }
  });
const zoomContainer = svg.call(zoom);

setTimeout(() => {
  const w = svg.property('width').baseVal.value;
  const h = svg.property('height').baseVal.value;
  const initialScale = Math.min((w - 25) / 500, h / 425);
  zoom.scaleTo(zoomContainer, initialScale);
  svg
    .select('g')
    .attr(
      'transform',
      `translate(${0.35 * (w - 275)}, ${45 /
        initialScale}) scale(${initialScale}, ${initialScale})`
    );
}, 200);

document.querySelector('.input-form').addEventListener('submit', triggerSearch);
document.querySelector('.retry-btn').addEventListener('click', e => {
  triggerSearch();
});

function triggerSearch(e) {
  if (e) e.preventDefault();
  const inicio = selects[0].selectedIndex;
  const fin = selects[1].selectedIndex;
  if (inicio <= 0) {
    selects[0].root_.classList.add('mdc-select--invalid');
    return;
  }
  if (fin <= 0) {
    selects[1].root_.classList.add('mdc-select--invalid');
    return;
  }
  const hora = document.querySelector('#hour-outlined').value || null;

  progress.open();

  fetchAndPaint({ inicio, fin, hora, transbordos: checkbox.checked });
}

function fetchAndPaint(params) {
  const endpoint = window.location.hostname.includes('localhost')
    ? 'http://localhost:4567'
    : 'https://tgt1qa590k.execute-api.eu-west-3.amazonaws.com/default/tokyoAEstrella';
  fetch(endpoint, {
    method: 'POST',
    body: JSON.stringify(params),
    headers: { 'content-type': 'application/json' },
  })
    .then(response => response.json())
    .then(({ result, lines, weight }) => {
      lines = lines.map(l => l - 1);
      let trans = 0;
      for (let i = 1; i < lines.length; i++)
        if (lines[i] !== lines[i - 1]) trans++;
      const undoPenalty = params.transbordos ? 100000 * trans : 0;

      if (
        lines.length >= 3 &&
        lines[lines.length - 1] !== lines[lines.length - 2]
      )
        lines[lines.length - 1] = lines[lines.length - 2];

      document.querySelector('#tube-map').classList.add('result');
      const resultMap = document.querySelector('#result-map');
      resultMap.classList.add('result');
      if (window.innerWidth > 700) {
        resultMap.style.display = 'inline-block';
      } else {
        resultMap.style.display = 'block';
      }
      resultMap.scrollIntoView({ behavior: 'smooth' });

      progress.close();

      const resultsDiv = document.querySelector('.results');
      resultsDiv.style.visibility = 'visible';
      resultsDiv.style.opacity = 1;
      resultsDiv.querySelector('.stations').innerText = result.length;
      resultsDiv.querySelector('.time').innerText = (
        ((weight - undoPenalty) / 40000) *
        60 *
        parseTime(params.hora)
      ).toFixed(1);
      resultsDiv.querySelector('.trans').innerText = trans;

      const tspans = Array.from(document.querySelectorAll('tspan'));
      tspans.forEach(el => (el.style.fontWeight = 'normal'));

      result
        .map(
          id =>
            Object.keys(data.stations).filter(
              k => Number(data.stations[k].id) === id
            )[0]
        )
        .forEach(name => {
          const element = tspans.filter(el => el.innerHTML === name)[0];
          element.style.fontWeight = 'bolder';
        });

      resultUnderMap(result, lines);
    })
    .catch(error => {
      console.error(error);
      progress.close();
      snackbar.open();
    });
}

function resultUnderMap(result, resultLines) {
  const stations = Object.fromEntries(
    Object.entries(data.stations)
      .filter(([k, v]) => result.includes(v.id) && v.label)
      .map(([k, v]) => [k, { label: v.label, id: v.id }])
  );

  const lines = [];
  let myNodes = [];
  let currentLine = {
    name: 'ResultX',
    label: 'NoneX',
    color: parseColor(resultLines[0]),
    shiftCoords: [0, 0],
    nodes: [],
  };
  for (let i = 0; i < result.length; i++) {
    const node = {
      coords: [0, i * -10],
      name: Object.entries(stations).filter(
        ([k, v]) => result[i] === v.id
      )[0][0],
      labelPos: i % 2 === 0 ? 'W' : 'E',
    };
    if (resultLines[i] !== resultLines[i - 1]) {
      node.marker = 'interchange';
    }
    myNodes.push(node);
    if (resultLines[i] !== resultLines[i - 1] && i !== 0) {
      currentLine.nodes = myNodes;
      lines.push(currentLine);
      myNodes = [node];
      currentLine = {
        name: `Result${i}`,
        label: `None${i}`,
        color: parseColor(resultLines[i]),
        shiftCoords: [0, 0],
        nodes: [],
      };
    }
  }
  myNodes[myNodes.length - 1].marker = 'interchange';
  currentLine.nodes = myNodes;
  lines.push(currentLine);

  const resultContainer = d3.select('#result-map');

  try {
    resultContainer
      .select('#result-map > svg')
      .data({})
      .exit()
      .remove();
  } catch (e) {}
  const resultMap = d3
    .tubeMap()
    .width(100)
    .height(50 * result.length)
    .margin({
      top: 0,
      right: 0,
      bottom: 0,
      left: 0,
    });

  resultContainer
    .datum({
      stations,
      lines,
    })
    .call(resultMap);
  const resultSvg = resultContainer.select('#result-map > svg');

  const zoom = d3
    .zoom()
    .scaleExtent([1, result.length])
    .on('zoom', () => {
      const offset = document.querySelector('#result-map').clientWidth / 2;
      resultSvg
        .select('g')
        .attr(
          'transform',
          `translate(${offset}, ${d3.event.transform.y})scale(${d3.event.transform.k})`
        );
    });
  const zoomContainer = resultSvg.call(zoom);

  setTimeout(() => {
    zoom.scaleTo(zoomContainer, Math.min(result.length, 5));
    zoom.translateTo(zoomContainer, 0, 0);
  }, 200);
}

function parseColor(id) {
  if (id === 0) return '#669934';
  if (id === 1) return '#ffcc66';
  if (id === 2) return '#ff3334';
}

function parseTime(hour) {
  if (!hour) return 1;
  hour = Number(hour.substr(0, 2)) + Number(hour.substr(3, 2)) / 60;
  if (hour >= 0 && hour < 5) return 1.25;
  if (hour >= 5 && hour < 6) return 1.15;
  if (hour >= 6 && hour < 8) return 1;
  if (hour >= 8 && hour < 12) return 1.15;
  if (hour >= 12 && hour < 16) return 0.85;
  if (hour >= 16 && hour < 22) return 0.75;
  if (hour >= 22 && hour <= 24) return 1.15;
}

async function test() {
  for (let i = 1; i <= 36; i++) {
    for (let j = 1; j <= 36; j++) {
      fetchAndPaint({ inicio: i, fin: j, hora: null, transbordos: false });
      await new Promise(resolve => setTimeout(resolve, 1000)); // 1 segundos
      fetchAndPaint({ inicio: i, fin: j, hora: null, transbordos: true });
      await new Promise(resolve => setTimeout(resolve, 1000)); // 1 segundos
    }
  }
}

// test();
