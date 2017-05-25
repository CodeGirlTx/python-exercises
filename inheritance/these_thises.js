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
  friends() {
    console.log(this.friends);
  }
  lazyGreet(other) {
    setTimeout(() => {console.log('Yo ' + other.name + '! from ' + this.name + '.')}, 2000);
  }
}


var Ashley = new Person('Ashley');
var Blake = new Person('Blake');
Ashley.addFriend(Blake);
Blake.addFriend(Ashley);
