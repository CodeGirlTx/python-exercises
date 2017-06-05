var promise = require('bluebird');
var pgp = require('pg-promise')({
  promiseLib: promise
});
var prompt = require('prompt-promise');
var musicdb = pgp({database: 'music'});
var query = "INSERT INTO track (id, track_number, duration, album_id) VALUES(default, ${track_number}, ${duration}, ${album_id})";

var tracks = {};

prompt('Track number? ')
  .then(function (val) {
    tracks.track_number = val;
    return prompt('duration? ');
  })
  .then(function (val) {
    tracks.duration = val;
    return prompt('Album id? ')
  })
  .then(function (val) {
    tracks.album_id = val;
    console.log(query);
    return musicdb.result(query, tracks)
  })
  .then(function (result) {
    console.log(result);
    pgp.end();
    prompt.done();
  })
  .catch(function rejected(err) {
    console.log('error', err.stack);
    prompt.finish();
  });
