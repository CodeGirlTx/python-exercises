mat1 = [[1, 2], [2, 3]];
mat2 = [[3, 2], [4, 5]];

function matrixAdd(add1, add2) {
  var sum = [];
  for (var i = 0; i < add1.length; i++) {
    var t = [];
    for (var j = 0; j < add1[i].length; j++) {
      t.push(add1[i][j] + add2[i][j]);
    }
    sum.push(t);
  }
  return sum;
}

console.log(matrixAdd(mat1, mat2));
