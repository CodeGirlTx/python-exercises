var fs = require('fs');
var readline = require('readline');
var filename = 'read_a_file.js'

var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

fs.readfile(filename, function(err, buffer) {
  if(err) {
    console.error(err.message);
  }
  var contents = buffer.toString().toUpperCase();
  console.log(contents);
  rl.close;
  })
