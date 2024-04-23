#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2] === undefined) {
  console.log('No argumnt');
}
argv.forEach((val, index) => {
  if (index >= 2) {
    console.log(val);
  }
});
