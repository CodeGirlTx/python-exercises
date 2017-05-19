var arr = [
  [1, 3, 4],
  [2, 4, 6, 8],
  [3, 6]
];

function sum(array) {
  array = array.reduce(function (x, y) {
  return x + y;
  });
  return array;
}

function sorted(array) {
  array.sort(function (a, b) {
    if (sum(a) > sum(b)) { return 1;}
    else if (sum(a) < sum(b)) { return -1;}
    return 0;
  });
}
