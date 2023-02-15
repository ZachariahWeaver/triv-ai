    let colCount = [5,5,5,5,5,5];
    let titles = document.getElementsByClassName("category-boxes");
    let clueCount = 2;
    let score = 0;
    let values = [200, 400, 600, 800, 1000];
    let timeLeft = 10;
    let timer;
    let buzzed = false;

function revealClue(row, col, clues) {
    var clue = clues[row][col];
    document.getElementById('activecluetext').innerText = clue;
    var x = document.getElementById('activeclue');
    x.style.display = 'flex';
    startTimer();
    // get the clicked clue box
    var clickedBox = event.target;
    // hide the clue box by setting its visibility property to "hidden"
    clickedBox.innerText = "";  // remove the text content
    clickedBox.removeAttribute("onclick");  // remove the onclick attribute
    updateColumns(col);
    score = score + values[row];
    console.log(row);

}

function hideClue(condition){
  var x = document.getElementById('activeclue');
    x.style.display = 'none'; //CHANGE SCORE BASED ON CONDITIONS
    console.log(condition);
    console.log(buzzed)
    updateCategories();

}

function updateColumns(col){


    console.log("column " + col + " is at " + colCount[col])
    colCount[col] = colCount[col]-1;
    if (colCount[col] === 0){
        titles[col].innerText = "";  // remove the text content
    }

}

function updateCategories(){
    clueCount = clueCount - 1;
    console.log(clueCount)
    if (clueCount === 0){
        document.getElementById('grid').style.display = 'none';
        document.getElementById('endCard').style.display = 'flex';
        document.getElementById("endgametext").innerHTML = "Game over <br>  SCORE: " + score;
    }
}

function submitAnswer() {
    var answer = document.getElementById("activeclueinput").value;
    console.log(answer);
    stopTimer();
    if(answer === answer){ // FIX VALIDATION
        hideClue("right")
    }
    else{
        hideClue("wrong")
    }
}

function startTimer() {
    buzzed = false;
  document.getElementById("timer").innerHTML = "Time remaining: " + timeLeft + " seconds";
  timer = setInterval(function() {
    timeLeft--;
    console.log(timeLeft);
    document.getElementById("timer").innerHTML = "Time remaining: " + timeLeft + " seconds";
    if (timeLeft <= 0) {
      clearInterval(timer);
      document.getElementById("timer").innerHTML = "Time's up!";
      hideClue("timeup");

    }
  }, 1000);
}
function stopTimer() {
  clearInterval(timer);
}

function buzzIn(){
        buzzed = true;
        activeclue.removeAttribute("onclick");  // remove the onclick attribute
        document.getElementById('submissionbox').style.display = "flex"
        timeLeft = timeLeft + 10;
}

