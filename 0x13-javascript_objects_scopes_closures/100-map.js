#!/usr/bin/node

// Imports an array and computes a new array.

/*
Read: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array
*/

const list = require('./100-data.js').list;
console.log(list);

const newList = list.map((x, i) => x * i);
console.log(newList);
