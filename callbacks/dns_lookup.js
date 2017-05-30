var fs = require('fs');
var dns = require('dns');
// var request = require('request');
var readline = require('readline');

var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("domain?", function(domain) {
  dns.lookup(domain, function (err, ipAddress) {
    if(err) {
      console.error(err.message);
      rl.close();
      return;
    }
  console.log(domain + "'s' ip addres is " + ipAddress);
  });
  rl.close();
});
