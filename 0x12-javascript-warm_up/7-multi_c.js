#!/usr/bin/node
const { argv } = require('node:process');
const arrlen = Number(argv[2]);

if (isNaN(arrlen)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < arrlen; i++) {
    console.log('C is fun');
  }
}
