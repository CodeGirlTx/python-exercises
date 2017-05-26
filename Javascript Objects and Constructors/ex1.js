function Person(name, email, phone) {
  this.name = name;
  this.email = email;
  this.phone = phone;
}

Person.prototype.greet = function greet(other) {
  console.log('Hello ' + other.name +', I am ' + this.name + '!');
}
var Sonny = new Person('Sonny', 'sonny@hotmail.com', '555-555-5555');
var Jordan = new Person('Jordan', 'jordan@aol.com', '444-444-4444');

Sonny.greet(Jordan);
Jordan.greet(Sonny);

Sonny
Jordan
