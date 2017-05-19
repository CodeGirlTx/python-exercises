arr1 = [1, 2, 3, 4, 5];

function evenNum(arr) {
  var even = arr.filter(function(item){
    return item % 2 === 0;
  });
  return even;
}

evenNum(arr1);
