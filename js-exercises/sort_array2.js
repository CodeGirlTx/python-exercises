function sorted(array) {
  array.sort(function (x, y) {
    if (x.length > y.length) { return 1;}
    else if (x.length < y.length) { return -1;}
    return 0;
  });
}

var fruit = [
  'banana',
  'orange',
  'kiwi',
  'apple',
  'lemon',
  'strawberry',
  'pineapple'
];
