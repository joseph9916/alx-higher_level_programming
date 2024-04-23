#!/usr/bin/node
const { argv } = require('node:process');
const arrlength = Number(argv[2]);
const text = 'X';

if (isNaN(arrlength)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arrlength; i++) {
    console.log(text.repeat(arrlength));
  }
}
