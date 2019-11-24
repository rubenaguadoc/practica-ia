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
if ('serviceWorker' in navigator) {
  const swName = '../sw.js';
  navigator.serviceWorker.register(swName, { scope: '/' }).catch(console.error);
}

const d3 = require('d3');
const tubeMap = require('d3-tube-map');
const originalData = require('../data/stations.json');
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
    select.value = String(originalData.stations[name].id);
    select.valid = true;
    select.foundation_.notchOutline(true);
    select.label_.float(true);
    if (lastSet === 1) {
      triggerSearch();
    }
  });

container.datum(originalData).call(map);

function adjustZoom() {
  const svg = container.select('#tube-map > svg');
  const zoom = d3
    .zoom()
    .scaleExtent([0.2, 2])
    .on('zoom', () => {
      svg.select('g').attr('transform', d3.event.transform.toString());
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
    // const initialTranslate = [0, 30];
    // zoom.translateTo(zoomContainer, initialTranslate[0], initialTranslate[1]);
  }, 200);
}

adjustZoom();

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
  console.log({ inicio, fin, hora, transbordos: checkbox.checked });
  progress.open();
  snackbar.open();
  setTimeout(() => {
    progress.close();
    const result = [1, 2, 3, 4, 5];

    const stations = result.map(
      id =>
        Object.keys(originalData.stations).filter(
          k => Number(originalData.stations[k].id) === id
        )[0]
    );
    // TODO: Search lines.nodes.coords where name in stations array
    console.log(stations);
    const data = Object.assign({}, originalData);
    data.lines.push({
      name: 'Result',
      label: 'None',
      color: 'blue',
      shiftCoords: [0, 0],
      nodes: [
        {
          coords: [0, -25],
        },
        {
          coords: [-4, -25],
        },
      ],
    });
    container
      .select('#tube-map > svg')
      .data(data)
      .exit()
      .remove();
    container.datum(data).call(map);
    adjustZoom();
  }, 2000);
}
