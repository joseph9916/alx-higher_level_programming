#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length <= 3) {
  console.log(0);
}
let num;
const arr = [];
for (let j = 2; j < argv.length; j++) {
  num = Number(argv[j]);
  if (!(isNaN(num))) {
    arr.push(num);
  }
}

if (arr.length === 2) {
  if (arr[0] < arr[1]) {
    console.log(arr[0]);
  } else {
    console.log(arr[1]);
  }
} else {
  let largest = Number(arr[0]);
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] >= largest) {
      largest = arr[i];
    }
  }
  let secondLargest = arr[0];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > secondLargest && arr[i] < largest) {
      secondLargest = arr[i];
    }
  }
  console.log(secondLargest);
}
