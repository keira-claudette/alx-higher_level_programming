#!/usr/bin/node

/*
returns the addition of 2 integers.
http://51elliot.blogspot.com/2012/01/simple-intro-to-nodejs-module-scope.html
*/

exports.add = function (a, b) {
  return (a + b);
};

const add = require('./13-add').add;
console.log(add(3, 5));
