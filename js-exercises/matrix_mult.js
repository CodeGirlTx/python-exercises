mat1 = [[1, 2], [2, 3]];
mat2 = [[3, 2], [4, 5]];

function matrixMultiply(mult1, mult2) {
  var mult = [];
  for (var i = 0; i < mult1.length; i++) {
    var t = [];
    for (var j = 0; j < mult1[i].length; j++) {
      t.push(mult1[i][j] * mult2[i][j]);
    }

  }
  return t;
}

console.log(matrixMultiply(mat1, mat2));
