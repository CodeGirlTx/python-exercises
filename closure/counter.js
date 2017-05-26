function counter () {
  var count = 0;
  var actuallyCount = function () {
    count++;
    return count;
  }
  return actuallyCount;
}


//counter 2

function counter2 (start) {
  var count = start;
  var actuallyCount = function () {
    count++;
    return count;
  }
  return actuallyCount;
}

//counter 3
function counter3 (start) {

  var count = start;
  var countActually = function () {
    count++;
    return count;
  }
  var countActually = function () {
    count--;
    return count;
  }

}

//counter 3

function counter(start) {
  var count = start;
  var aCount = function (start) {

    return {
      increment:function(){count++; return count},
      decrement:function(){count--; return count}
    }
  }
  return aCount();
}
