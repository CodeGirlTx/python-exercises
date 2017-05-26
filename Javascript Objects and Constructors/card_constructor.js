function Card(point, suit) {
  this.point = point;
  this.suit = suit;

}

Card.prototype.getImageUrl = function () {
  return "images/" + myCard.point + "_of_" + myCard.suit + ".png";
}

var myCard = new Card(10, 'clubs');

myCard.point

myCard.suit



myCard.getImageUrl();
