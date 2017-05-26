class Hand {
  constructor(name) {
    this.name = name;
    this.cards = [];
  }

  addCard(card) {
    this.cards.push(card);
  }

  getPoints() {
    var cardArray = this.cards;
    var pointsTotal = 0;
    for(var i = 0; i < cardArray.length; i++) {
      pointsTotal += cardArray[i].points;
    }
    return pointsTotal;
  }
}

class Card {
  constructor (points, suit) {
  this.points = points;
  this.suit = suit;
  }
}

// class Deck {
//   constructor(name){
//     this.name = name;
//     this.deck = [];
//
//     var label = ['2','3','4','5','6','7','8','9','10','jack','queen','king','ace'];
//     var suit = ['clubs','spades','diamonds','hearts'];
//     var deckArray = this.deck;
//     label.forEach(function(label) {
//       suit.forEach(function(suit) {
//         deckArray.push({'label': label, 'suit':suit, 'img':label + '_of_' + suit + '.png'})
//       });
//     });
//
//   draw() {
//
//   }
//   shuffle() {
//
//   }
//   numCardsLeft() {
//
//   }
//
//   }
// }
var myHand = new Hand();
myHand.addCard(new Card(5, 'diamonds'));
myHand.addCard(new Card(10, 'hearts'));

myHand.getPoints();


// return this.friends.map(function (other) {
//   return other.name;
// });


// var myHand = new Hand()
//
// myHand.addCard(new Card())
