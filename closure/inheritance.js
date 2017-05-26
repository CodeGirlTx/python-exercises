var mom = {
  fname: 'Alice',
  lname: 'Wong',
  eyecolor: 'brown',
  haircolor: 'black'
};
var daughter = {
  fname: 'Ilene',
  haircolor: 'brown'
};

class Mom {
  constructor(fname, lname, eyecolor, haircolor) {
    this.fname = fname;
    this.lname = lname;
    this.eyecolor = eyecolor;
    this.haircolor = haircolor;
  }

}

class Daughter extends Mom {
  features() {
    console.log("Daughter Features: ", this.fname, this.lname, this.eyecolor, this.haircolor);
  }
}
var m = new Mom('Karen', 'Wong', 'black', 'black');

var d = new Daughter('Kristine', m.lname, m.eyecolor, 'brown');

d.features();
