#!/usr/bin/node

// Describes a class Square that defines a square and inherits from Rectangle

/*
----------- THIS WORKS TOO -----------
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
*/

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super();
    this.width = size;
    this.height = size;
  }
}

module.exports = Square;
