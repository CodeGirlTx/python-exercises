function print_square(num) {
  st = "*";
  for (var i = 0; i < num; i++) {
    console.log(st.repeat(num));
  }
}

function print_box(width, height) {
  var st = "*".repeat(width);
  console.log(st)
  var st2 = "*" + " ".repeat(width - 2) + "*";
  for (var i = 0; i < height; i++) {
    console.log(st2);
  }
  console.log(st);
}

function print_banner(message) {
  var firstL = "**" + "*".repeat(message.length) + "**";
  console.log(firstL);
  console.log("* " + message + " *");
  console.log(firstL);
}
