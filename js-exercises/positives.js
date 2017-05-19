function positiveNumbers(numbers) {
  var pos = numbers.filter(function(num) {
    return num > 0;
  });
  return pos;
}
