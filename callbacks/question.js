var readline = require('readline');

var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Question??? ', function(q) {
  console.log(q);
  console.log(42);
  
  rl.question('Question??? ', function(q) {
    console.log(q);
    console.log(42);
    rl.close();
  });
});


console.log('end of file');
