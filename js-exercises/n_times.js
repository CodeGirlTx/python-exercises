function callNTimes(a, b) {
  for (i=0; i < a; i++) {
    b()
  }
}


function hello() {
  console.log("hello world");
}
