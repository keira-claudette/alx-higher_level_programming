#!/usr/bin/node

const process = require('process');

const args = process.argv;

let i = Number(args[2]);

if (isNaN(i)) {
  console.log('Not a number');
} else {
  console.log('My number:', i);
}
