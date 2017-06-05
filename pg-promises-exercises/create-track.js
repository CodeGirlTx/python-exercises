var promise = require('bluebird');
var pgp = require('pg-promise')({
  promiseLib: promise
});
var co = require('co');
var prompt = require('prompt-promise');

co(function * genPrompt() {
  var trackName = prompt('Track name? ');
  return trackName;
  var musicdb = pgp({database: 'music'});
  var query = "INSERT INTO album VALUES(default, $1)";
  musicdb.result(query, name)
    .then(function (result) {
      console.log(result);
    });
})

.then(function fulfilled(name) {
  console.log('artist_name:', name);
  prompt.end();
})
.catch(function rejected(err) {
  console.log('error:', err.stack);
  prompt.finish();
});
