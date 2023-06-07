let colCount = [5,5,5,5,5,5];
let titles = document.getElementsByClassName("category-boxes");
let clueCount = 30;
let score = 0;
let values = [200, 400, 600, 800, 1000];
let timer;
let buzzed = false;
let clueStatus = [];
let clueset_num = document.querySelector('.title').getAttribute('data-clueset-num');
let activerow = 0;
let toggled = false;
for (let i = 0; i < 6; i++) {
    clueStatus[i] = [false, false, false, false, false];

}


function revealClue(col, row, clues, responses) {
var clue = clues[col][row];
var response = responses[col][row];
clueStatus[col][row] = true;
document.getElementById('activecluetext').innerText = clue;
document.getElementById('activeclueresponse').innerText = response;
activerow = row;

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
activeclue.setAttribute('onclick', 'buzzIn()' );
}

function hideClue(condition){
var z = document.getElementById('activecluecontainer');
z.style.display = 'none';
var y = document.getElementById('grid')
y.style.display = 'grid'
var x = document.getElementById('submissionbox')
x.style.visibility = 'hidden'
updateCategories();
if(condition == "timeup"){
    if(buzzed){
        score = score - values[activerow];
    }
}
else if(condition == "right"){
    score = score + values[activerow];
}
else if(condition == "wrong"){
    score = score - values[activerow];
}

saveState();
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
    gameOverScreen();
    }
}
function gameOverScreen(){
    document.getElementById('grid').style.display = 'none';
    document.getElementById('endcardcontainer').style.display = 'flex';
    document.getElementById("endgametext").innerHTML = "Game over <br>  SCORE: " + score;
}
function submitAnswer() {
var guess = document.getElementById("activeclueinput").value;
var response = document.getElementById("activeclueresponse").value;
stopTimer();
if(guess == response){
    hideClue("right")
}
else{
    hideClue("wrong")
}
}
function toggleArchive(){
    var menu = document.getElementById("archivemenu");
    var button = document.getElementById("navbutton");
    if (toggled){
        menu.style.right = "-20vw";
        toggled = false;
    }
    else{
        menu.style.right = "0";
        toggled = true;
    }
    console.log("toggle");
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
    buzzed = true;
    timeLeft = 10;
    activeclue.removeAttribute('onclick');  // remove the onclick attribute
    document.getElementById('submissionbox').style.visibility = "visible"
}


function saveState() {
    let state = {
        colCount: colCount,
        clueCount: clueCount,
        score: score,
        clueStatus: clueStatus
    };
    clueset_number = getClueSetNumber();
    localStorage.setItem('gameState' + clueset_number, JSON.stringify(state));
}


function loadState() {
    console.log("loaded state")
    clueset_number = getClueSetNumber();
    console.log(clueset_number)
    let savedState = localStorage.getItem('gameState' + clueset_number);

    if (savedState !== null) {
        savedState = JSON.parse(savedState);
        colCount = savedState.colCount;
        clueCount = savedState.clueCount;
        score = savedState.score;
        clueStatus = savedState.clueStatus;  // Load the clue status
        if (clueCount === 0){
            gameOverScreen();
            }
        // Loop through the clueStatus array and hide clues that have been clicked
        for (let col = 0; col < clueStatus.length; col++) {
            for (let row = 0; row < clueStatus[col].length; row++) {
                if (clueStatus[col][row]) {
                    let clueElement = document.getElementById(`clue-${col}-${row}`);
                    if (clueElement) {
                        clueElement.innerText = "";  // remove the text content
                        clueElement.removeAttribute("onclick");  // remove the onclick attribute
                    }
                }
            }
        }
    }
}



function getClueSetNumber(){
    return clueset_num;
}
window.onload = function() {
    loadState();
}