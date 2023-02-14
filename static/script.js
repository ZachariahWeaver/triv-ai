function revealClue(clue) {
    document.getElementById('activecluetext').innerText = clue;

    var x = document.getElementById('activeclue');

    x.style.display = 'flex';


      // get the clicked clue box
    var clickedBox = event.target;
     // hide the clue box by setting its display property to "none"
    clickedBox.style.visibility = "hidden";
    }



function hideClue(){
  var x = document.getElementById('activeclue');
    x.style.display = 'none';

    }