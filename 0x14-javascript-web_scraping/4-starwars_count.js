#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const y = JSON.parse(body).results[0].characters;
  const x = y.filter(y => y.includes('18'));
  request(x[0], function (error, response, body) {
    if (error) {
      console.error(error);
    }
    console.log(JSON.parse(body).films.length);
  });
});
