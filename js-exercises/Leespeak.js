function leetspeak(str) {
  str = str.toUpperCase();
  let letters = {
    A: '4',
    E: '3',
    G: '6',
    I: '1',
    O: '0',
    S: '5',
    T: '7'
  }
  for(var i = 0; i < str.length; i++) {
    if (letters.hasOwnProperty(str[i])) {
      str = str.replace(str[i], letters[str[i]]);
    }
  }
  return str;
}
