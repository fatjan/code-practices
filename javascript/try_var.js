function looping() {
    for (var i = 0; i < 5; i++) {
      console.log(i); // 0 1 2 3 4 5
    }
    function inLooping() {
      console.log('ini i',i); // 5
    }
    inLooping();
  }
  looping();
