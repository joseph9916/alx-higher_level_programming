#!/usr/bin/node
const { argv } = require('node:process');
const num = Number(argv[2]);

function fact (num) {
  if (num === 1 || num === 0 || isNaN(num)) { return 1; }
  return num * fact(num - 1);
}
console.log(fact(num));
