function sum(array) {
  array = array.reduce(function (x, y) {
  return x + y;
  });
  return array;
}

var arr = [1, 2, 3, 100, 39, 20, 49, 2];
