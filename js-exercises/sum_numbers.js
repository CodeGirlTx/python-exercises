function sumNumbers(numbers) {
  var array = numbers.split(',');
  for (var i=0; i < numbers.length; i++) {
    sumArray = sum(array);
  }
  return sum;
}

function sumNumbers(numbers) {
  var sum = 0;
  numbers.forEach(function(item) {
    sum += item;
  });
  return sum;
}
