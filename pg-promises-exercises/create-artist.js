var promise = require('bluebird');
var pgp = require('pg-promise')({
  promiseLib: promise
});
var prompt = require('prompt-promise');
var musicdb = pgp({database: 'music'});
var query = "INSERT INTO artist VALUES(default, $1)";
var artist;

prompt('Artist name? ')
  .then(function (val) {
  console.log(query);
  return musicdb.result(query, val);
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
