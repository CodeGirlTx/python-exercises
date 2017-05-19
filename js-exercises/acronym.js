arr1 = ['national', 'aeronautics', 'space', 'administration'];


//with CharAt
var acronym = function (letter) {
  newArray = [];
  for (var i = 0; i < letter.length; i += 1) {
      var array = letter[i].charAt(0);
      newArray.push(array);
    }
    return newArray;
}

//with reduce

function acronym (x, y) {
  console.log(x, y);
  return x + y.charAt(0);
}

arr1.reduce(acronym, '')
