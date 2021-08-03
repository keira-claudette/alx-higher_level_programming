#!/usr/bin/node

// Defines an empty class that defines a rectangle

/*
This tests for module dependecies. module.exports vs exports
Excluding  module.exports from this module raises a TypeError exception:
"Rectangle is not a constructor" when 0-main.js test is run.
Running tests in 0-main.js as scripts in this module produces what's expected
implying 0-main.js failing is an importing issue

Read: https://www.sitepoint.com/understanding-module-exports-exports-node-js/
*/

class Rectangle {}

module.exports = Rectangle;
