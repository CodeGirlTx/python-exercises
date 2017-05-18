function factors(num) {
  var str = "0";
  for (var i = 1; i <= num; i++) {
    if (num % i == 0)  {
      str += ',' + i;
    }
  }
  console.log(str);
}
