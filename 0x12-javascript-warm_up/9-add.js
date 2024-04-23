#!/usr/bin/node
const { argv } = require('node:process');
const num1 = Number(argv[2]);
const num2 = Number(argv[3]);

function add (a, b) {
  const result = a + b;
  return result;
}
if (isNaN(num1) || isNaN(num2)) {
  console.log(NaN);
} else {
  console.log(add(num1, num2));
}
