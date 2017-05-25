class Person {
  constructor(name) {
    this.name = name;
    this.friends = [];
  }
  addFriend(friend) {
    this.friends.push(friend);
  }
  createGreeting(other) {
    return 'Yo ' + other.name + '! from ' + this.name + '.';
  }
  friends() {
    console.log(this.friends);
  }
  lazyGreet(other) {
    setTimeout(() => {console.log('Yo ' + other.name + '! from ' + this.name + '.')}, 2000);
  }
  createGreetingsForFriends() {
    //return this.friends.map((other) => { return this.createGreeting(other) });
    var self = this;
    return this.friends.map(function (other) {
      return self.createGreeting(other);
    });
  }
}


var Ashley = new Person('Ashley');
var Blake = new Person('Blake');
Ashley.addFriend(Blake);
Blake.addFriend(Ashley);
