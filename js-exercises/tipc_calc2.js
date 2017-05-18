function totalAmount(amount, service){
  

}







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
