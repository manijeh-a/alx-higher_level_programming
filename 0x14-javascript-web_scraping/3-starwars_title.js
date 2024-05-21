#!/usr/bin/node
const https = require('https');
const episodeNum = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/films/';
https.get(API_URL + episodeNum, (res) => {
  if (res.statusCode === 200) {
    let data = '';
    res.on('data', (chunk) => {
      data += chunk;
    });
    res.on('end', () => {
      const responseJSON = JSON.parse(data);
      console.log(responseJSON.title);
    });
  } else {
    console.log(`Error code: ${res.statusCode}`);
  }
}).on('error', (err) => {
  console.log(err);
});
