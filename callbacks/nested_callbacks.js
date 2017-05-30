// function square(num) {
//   return num * num;
// }
//
// var squared = square(5);




// var x = 4;
// var y = 3;
// var x2 = square(x);
// var y2 = square(y);
// var sum = x2 + y2;

function square(num, callback) {
  var squared = num * num;
  callback(num);
});


function sum(y, x, callback) {
  callback(x + y);
});

square(4, function (x2) {
  square(3, function(y2) {
    sum(x2, y2, function (ans){
      console.log(ans);
    })
  })
})

function square(num, callback) {
  setTimeout(function() {
    var ans = num * num;
    callback(ans);
  }, 1000);
}

function squareRoot(num, callback) {
  setTimeout(function() {
  var root = Math.sqrt(num);
  callback(root);
  }, 500);
}

square(4, function (x2) {
  square(3, function(y2) {
    sum(x2, y2, function (sum){
      squareRoot(sum, function(ans) {
      console.log("The answer is: " + ans);
      });
    });
  });
});
