class Person {
  constructor(name) {
    this.name = name;
    this.friends = [];
  }
  addFriend(friend) {
    this.friends.push(friend);
  }
  createGreeting(other) {
    console.log('Yo ' + other.name + '! from ' + this.name + '.');
  }
  friendsNames() {
  return this.friends.map(function (other) {
    return other.name;
  });
  }
}


var Ashley = new Person('Ashley');
var Blake = new Person('Blake');
var Anthony = new Person('Anthony');

Ashley.addFriend(Blake);
Blake.addFriend(Ashley);
Ashley.addFriend(Anthony);


Ashley.friendsNames();

// friends(Ashley);

// class Friend extends Person {
//   createGreeting(other) {
//     console.log('Yo ' + other.name + '! from ' + this.name + '.');
//   }
// }
