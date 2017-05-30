var dns = require('dns');
var host = 'digitalcrafts.com';

dns.lookup(host, function (error, ip) {
console.log(ip);
});
