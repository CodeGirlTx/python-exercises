// CPS FUNCTION REWRITES

function add(x, y, callback) {
var result = x + y;
return (result);
}

function subtract(x, y, callback) {
  var result = x - y;
  callback(result);
}

function greeting(person, callback) {
  var result = 'hello, ' + person + '!';
  callback(result);
}

function hello(callback) {
  console.log('Hello, world!');
  callback();

}

function product(numbers, callback) {
  var result = numbers.reduce(function(a, b) {
    return a * b;
  }, 1);
  callback(result);
}
