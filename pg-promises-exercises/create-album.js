var promise = require('bluebird');
var pgp = require('pg-promise')({
  promiseLib: promise
});
var co =require('co');
var prompt = require('prompt-promise');
var musicdb = pgp({database: 'music'});

var query = "INSERT INTO album VALUES(default, ${name}, ${released}, ${artist_id})";
//$1 stands for first argument (name) if you had db.result(query, name, address) then address would be $2

var album = {};

prompt('Album name? ')
.then(function albumName(val) {
  album.name = val;
  return prompt('Album year? ');
})
.then(function albumYear(val) {
  album.released = val;
  return prompt('Artist id? ');
})
.then(function artistId(val) {
  album.artist_id = val;

  console.log(query);
  return musicdb.result(query, album);
})
.then(function (result) {
  console.log(result);
  pgp.end();
  prompt.done();
})
.catch(function rejected(err) {
  console.log('error:', err.stack);
  prompt.finish();
});
