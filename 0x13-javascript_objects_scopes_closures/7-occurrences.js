#!/usr/bin/node

// Describes function that returns the number of occurrences in a list

/*
Read: https://www.w3resource.com/javascript-exercises/fundamental/javascript-fundamental-exercise-70.php
*/

exports.nbOccurences = function (list, searchElement) {
  return (list.reduce((a, v) => (v === searchElement ? a + 1 : a), 0));
};
