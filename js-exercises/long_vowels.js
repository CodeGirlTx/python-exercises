function long_vowels(str) {
  var arrayOne = ["aa", "ee", "ii", "oo", "uu"];
  var arrayTwo = ["aaaaa", "eeeee", "iiiii", "ooooo", "uuuuu"];
  for (var i = 0; i < str.length; i++) {
    str = str.replace(arrayOne[i], arrayTwo[i]);
  }
  return str;
}
