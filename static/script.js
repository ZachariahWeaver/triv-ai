let colCount = [5,5,5,5,5,5];
let titles = document.getElementsByClassName("category-boxes");
let clueCount = 30;
let score = 0;
let values = [200, 400, 600, 800, 1000];
let timer;
let buzzed = false;

function revealClue(col, row, clues) {
var clue = clues[col][row];
document.getElementById('activecluetext').innerText = clue;
var z = document.getElementById('activecluecontainer');
z.style.display = 'flex';
var y = document.getElementById('grid')
y.style.display = 'none'
startTimer();
// get the clicked clue box
var clickedBox = event.target;
// hide the clue box by setting its visibility property to "hidden"
clickedBox.innerText = "";  // remove the text content
clickedBox.removeAttribute("onclick");  // remove the onclick attribute
updateColumns(col);
score = score + values[row];
activeclue.setAttribute('onclick', 'buzzIn()' );
}

function hideClue(condition){
var z = document.getElementById('activecluecontainer');
z.style.display = 'none';
var y = document.getElementById('grid')
y.style.display = 'grid'
var x = document.getElementById('submissionbox')
x.style.display = 'none'
updateCategories();
document.getElementById('activeclueinput').value = ''

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
    document.getElementById('endcardcontainer').style.display = 'flex';
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
timeLeft = 10;
document.getElementById("timer").innerHTML = timeLeft;
timer = setInterval(function() {
timeLeft--;
console.log(timeLeft);
document.getElementById("timer").innerHTML = timeLeft;
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
    timeLeft = 10;
    activeclue.removeAttribute('onclick');  // remove the onclick attribute
    document.getElementById('submissionbox').style.display = "block"
}

function nothing(){
    1+1;
}