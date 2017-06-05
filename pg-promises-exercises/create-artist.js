var promise = require('bluebird');
var pgp = require('pg-promise')({
  promiseLib: promise
});
var co = require('co');
var prompt = require('prompt-promise');
var musicdb = pgp({database: 'music'});
var query = "INSERT INTO artist VALUES(default, $1)";

co(function * genPrompt() {
  var name = prompt('Artist name? ');
  return name;
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
