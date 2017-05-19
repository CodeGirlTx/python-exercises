function rockPaper(player1, player2) {
  if (player1 === 'rock' && player2 === 'scissors') {
    console.log('player2');
  }
  else if (player1 === player2) {
    console.log('draw');
  }
  else if (player1 === 'paper' && player2 === 'rock') {
    console.log('player1')
  }
  else if (player1 === 'scissors' && player2 === 'paper') {
    console.log('player1');
  }
  else {
    console.log('player2');
  }
}

rockPaper('paper', 'rock')
