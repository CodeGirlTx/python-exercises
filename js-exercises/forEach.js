var arr1 = [
  { name: 'Bob' },
  { name:'Alice' },
  { name:'Joe' }
];

function forEach(arr, fun) {
  for (i = 0; i < arr.length; i++) {
   fun(arr[i]);
  }
}

forEach(arr1, function(person) {
  console.log('Hello, ' + person.name + '!');
});
