#!/usr/bin/node

// converts a number from base 10 to another base passed as argument

/*

Read: https://javascript.plainenglish.io/number-base-conversion-in-javascript-8bc44219b4ab#:~:text=It%20is%20possible.,required%20base%20using%20toString()%20.
*/

exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
