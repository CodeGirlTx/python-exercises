
// exercise 1

function hello(name) {
  console.log('hello ' + name);
}
hello('ronda');



// ****************************
//exercise 2
var name = prompt("What is your name?");

function hello(name) {
  if (name != null) {
  console.log('hello ' + 'world');
}  else {
  console.log('hello ' + name)
  }
}

//*******************************

//exercise 3 madlib
function madlib(name, subject) {
  return (name + "'s favorite subject is " + subject);
}

//exercise 4 tip calculator

function tipAmount(amount, service) {
  var tip = tip;
  if (service === 'bad') {
    tip = (amount * 10) / 100;
    return tip;
  }
  if (service === 'fair') {
    tip = (amount * 15) / 100;
    return tip;
  }
  if (service === 'good') {
    tip = (amount * 20) / 100;
    return tip;
  }
}

tipAmount(20, 'bad');
