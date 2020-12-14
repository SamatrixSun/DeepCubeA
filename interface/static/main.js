var state = [];
var rotateIdxs_old = null;
var rotateIdxs_new = null;
var stateToFE = null;
var FEToState = null;
var legalMoves = null;

var solveStartState = [];
var solveMoves = [];
var solveMoves_rev = [];
var solveIdx = null;
var solution_text = null;

var faceNames = ["top", "bottom", "left", "right", "back", "front"];
var colorMap = {0: "#ffffff", 1: "#ffff1a", 4: "#0000ff", 5: "#33cc33", 2: "#ff8000",3: "#e60000"};
var corners =  [1842, 62045, 22944, 82747, 92651, 152436, 113353, 173538];
var sides = [143, 319, 528, 746, 1052, 1225, 1637, 1434, 2139, 2348, 3241, 3050];
var lastMouseX = 0,
  lastMouseY = 0;
var rotX = -30,
  rotY = -30;

var moves = []

function reOrderArray(arr,indecies) {
	var temp = []
	for(var i = 0; i < indecies.length; i++) {
		var index = indecies[i]
		temp.push(arr[index])
	}

	return temp;
}

/*
	Rand int between min (inclusive) and max (exclusive)
*/
function randInt(min, max) {
	return Math.floor(Math.random() * (max - min)) + min;
}

function clearCube() {
  for (i = 0; i < faceNames.length; i++) {
    var myNode = document.getElementById(faceNames[i]);
    while (myNode.firstChild) {
      myNode.removeChild(myNode.firstChild);
    }
  }
}

function setStickerColors(newState) {
	state = newState
  clearCube()

  idx = 0
  for (i = 0; i < faceNames.length; i++) {
    for (j = 0; j < 9; j++) {
      var iDiv = document.createElement('div');
      iDiv.className = 'sticker';
      iDiv.style["background-color"] = colorMap[Math.floor(newState[idx]/9)]
      document.getElementById(faceNames[i]).appendChild(iDiv);
      idx = idx + 1
    }
  }
}

function buttonPressed(ev) {
	var face = ''
	var direction = '1'

	if (ev.shiftKey) {
		direction = '-1'
	}
	if (ev.which == 85 || ev.which == 117) {
		face='U'
	} else if (ev.which == 68 || ev.which == 100) {
		face = 'D'
	} else if (ev.which == 76 || ev.which == 108) {
		face = 'L'
	} else if (ev.which == 82 || ev.which == 114) {
		face = 'R'
	} else if (ev.which == 66 || ev.which == 98) {
		face = 'B'
	} else if (ev.which == 70 || ev.which == 102) {
		face = 'F'
	}
	if (face != '') {
		clearSoln();
		moves.push(face + "_" + direction);
		nextState();
	}
}


function enableScroll() {
	document.getElementById("first_state").disabled=false;
	document.getElementById("prev_state").disabled=false;
	document.getElementById("next_state").disabled=false;
	document.getElementById("last_state").disabled=false;
}

function disableScroll() {
	document.getElementById("first_state").blur(); //so keyboard input can work without having to click away from disabled button
	document.getElementById("prev_state").blur();
	document.getElementById("next_state").blur();
	document.getElementById("last_state").blur();

	document.getElementById("first_state").disabled=true;
	document.getElementById("prev_state").disabled=true;
	document.getElementById("next_state").disabled=true;
	document.getElementById("last_state").disabled=true;
}

/*
	Clears solution as well as disables scroll
*/
function clearSoln() {
	solveIdx = 0;
	solveStartState = [];
	solveMoves = [];
	solveMoves_rev = [];
	solution_text = null;
	document.getElementById("solution_text").innerHTML = "Solution:";
	disableScroll();
}

function setSolnText(setColor=true) {
	solution_text_mod = JSON.parse(JSON.stringify(solution_text))
	if (solveIdx >= 0) {
		if (setColor == true) {
			solution_text_mod[solveIdx] = solution_text_mod[solveIdx].bold().fontcolor("blue")
		} else {
			solution_text_mod[solveIdx] = solution_text_mod[solveIdx]
		}
	}
	document.getElementById("solution_text").innerHTML = "Solution: "+ solution_text_mod.join(" ");
}

function enableInput() {
	document.getElementById("scramble").disabled=false;
	document.getElementById("solve").disabled=false;
	document.getElementById("string_state").disabled=false;
	$(document).on("keypress", buttonPressed);
}

function disableInput() {
	document.getElementById("scramble").disabled=true;
	document.getElementById("solve").disabled=true;
	document.getElementById("string_state").disabled=true;
	$(document).off("keypress", buttonPressed);
}

function nextState(moveTimeout=0) {
	if (moves.length > 0) {
		disableInput();
		disableScroll();
		move = moves.shift() // get Move
		
		//convert to python representation
		state_rep = reOrderArray(state,FEToState)
		newState_rep = JSON.parse(JSON.stringify(state_rep))

		//swap stickers
		for (var i = 0; i < rotateIdxs_new[move].length; i++) {
			newState_rep[rotateIdxs_new[move][i]] = state_rep[rotateIdxs_old[move][i]]
		}

		// Change move highlight
		if (moveTimeout != 0){ //check if nextState is used for first_state click, prev_state,etc.
				solveIdx++
				setSolnText(setColor=true)
		}

		//convert back to HTML representation
		newState = reOrderArray(newState_rep,stateToFE)

		//set new state
		setStickerColors(newState)

		//Call again if there are more moves
		if (moves.length > 0) {
			setTimeout(function(){nextState(moveTimeout)}, moveTimeout);
		} else {
			enableInput();
			if (solveMoves.length > 0) {
				enableScroll();
				setSolnText();
			}
		}
	} else {
		enableInput();
		if (solveMoves.length > 0) {
			enableScroll();
			setSolnText();
		}
	}
}

function scrambleCube() {
	disableInput();
	clearSoln();

	numMoves = randInt(100,200);
	for (var i = 0; i < numMoves; i++) {
		moves.push(legalMoves[randInt(0,legalMoves.length)]);
	}

	nextState(0);
}

function judgeState() {
	var stateArray = [];
	for (var i = 0; i < 54; i++){
		stateArray[i] += 1;
		stateArray[state[i]] -= 1;
	}
	for (i = 0; i<54; i++){
		if stateArray[i]{
			return false;
		}
	}
	return true;
}

function stringInput(){
	var stateString = document.getElementById("input_state").value;
	for (var i = 0; i < 54; i++){
		state[i] = parseInt(stateString[2*i]);
	}
	string2State()
}

function string2State() {
	var large = 0
	var mid = 0
	var small = 0
	var t = 0
	/*var stateArray = document.getElementById("input_state").value.split(", ");
	for (var i = 0; i<54; i++){
		state[i] = parseInt(stateArray[i]);
	}
	document.getElementById("solution_text").innerHTML = state;
}*/
	for (var j = 0; j < 8; j++){
		large = corners[j] % 100;
		mid = Math.floor(corners[j]/100) % 100;
		small = Math.floor(corners[j]/10000);
		if (state[small]>state[mid]){
			t = mid;
			mid = small;
			small = t;
		}
		if (state[small]>state[large]){
			t = large;
			large = small;
			small = t;
		}
		if (state[mid]>state[large]){
			t = large;
			large = mid;
			mid = t;
		}
		if (state[small] == 0){
			if (state[mid] == 2){
				if (state[large] == 4){
					state[small] = 2;
					state[mid] = 20;
					state[large] = 44;
				}
				if (state[large] == 5){
					state[small] = 0;
					state[mid] = 26;
					state[large] = 47;
				}
			}
			if (state[mid] == 3){
				if (state[large] == 4){
					state[small] = 8;
					state[mid] = 35;
					state[large] = 38;
				}
				if (state[large] == 5){
					state[small] = 6;
					state[mid] = 29;
					state[large] = 53;
				}
			}
		}
		if (state[small] == 1){
			if (state[mid] == 2){
				if (state[large] == 4){
					state[small] = 9;
					state[mid] = 18;
					state[large] = 42;
				}
				if (state[large] == 5){
					state[small] = 11;
					state[mid] = 24;
					state[large] = 45;
				}
			}
			if (state[mid] == 3){
				if (state[large] == 4){
					state[small] = 15;
					state[mid] = 33;
					state[large] = 36;
				}
				if (state[large] == 5){
					state[small] = 17;
					state[mid] = 27;
					state[large] = 51;
				}
			}
		}
	}
	for (var k = 0; k<12; k++){
		small = sides[k] % 100;
		large = Math.floor(sides[k] / 100);
		if (state[small]>state[large]){
			t = large;
			large = small;
			small = t;
		}
		if (state[small] == 0){
			if (state[large] == 2){
				state[small] = 1;
				state[large] = 23;
			}
			if (state[large] == 3){
				state[small] = 7;
				state[large] = 32;
			}
			if (state[large] == 4){
				state[small] = 5;
				state[large] = 41;
			}
			if (state[large] == 5){
				state[small] = 3;
				state[large] = 50;
			}
		}
		if (state[small] == 1){
			if (state[large] == 2){
				state[small] = 10;
				state[large] = 21;
			}
			if (state[large] == 3){
				state[small] = 16;
				state[large] = 30;
			}
			if (state[large] == 4){
				state[small] = 12;
				state[large] = 39;
			}
			if (state[large] == 5){
				state[small] = 14;
				state[large] = 48;
			}
		}
		if (state[small] == 2){
			if (state[large] == 4){
				state[small] = 19;
				state[large] = 43;
			}
			if (state[large] == 5){
				state[small] = 25;
				state[large] = 46;
			}
		}
		if (state[small] == 3){
			if (state[large] == 4){
				state[small] = 34;
				state[large] = 37;
			}
			if (state[large] == 5){
				state[small] = 28;
				state[large] = 52;
			}
		}
	}
	state[4] = 4;
	state[13] = 13;
	state[22] = 22;
	state[31] = 31;
	state[40] = 40;
	state[49] = 49;
	if judgeState(){
		setStickerColors(state)
		document.getElementById("solution_text").innerHTML = "Input Finished!";
	}
	else{
		document.getElementById("solution_text").innerHTML = "Input Invalid!";
	}
}

function solveCube() {
	disableInput();
	clearSoln();
	document.getElementById("solution_text").innerHTML = "SOLVING...";
	$.ajax({
		url: '/solve',
		data: {"state": JSON.stringify(state)},
		type: 'POST',
		dataType: 'json',
		success: function(response) {
			solveStartState = JSON.parse(JSON.stringify(state))
			solveMoves = response["moves"];
			solveMoves_rev = response["moves_rev"];
			solution_text = response["solve_text"];
			solution_text.push("SOLVED!")
			setSolnText(true);

			moves = JSON.parse(JSON.stringify(solveMoves))

			setTimeout(function(){nextState(500)}, 500);
		},
		error: function(error) {
				console.log(error);
				document.getElementById("solution_text").innerHTML = "..."
				setTimeout(function(){solveCube()}, 500);
		},
	});
}

$( document ).ready($(function() {
	disableInput();
	clearSoln();
	$.ajax({
		url: '/initState',
		data: {},
		type: 'POST',
		dataType: 'json',
		success: function(response) {
			setStickerColors(response["state"]);
			rotateIdxs_old = response["rotateIdxs_old"];
			rotateIdxs_new = response["rotateIdxs_new"];
			stateToFE = response["stateToFE"];
			FEToState = response["FEToState"];
			legalMoves = response["legalMoves"]
			enableInput();
		},
		error: function(error) {
			console.log(error);
		},
	});
	
	$("#cube").css("transform", "translateZ( -100px) rotateX( " + rotX + "deg) rotateY(" + rotY + "deg)"); //Initial orientation	

	$('#scramble').click(function() {
		scrambleCube()
	});

	$('#solve').click(function() {
		solveCube()
	});

	$('#first_state').click(function() {
		if (solveIdx > 0) {
			moves = solveMoves_rev.slice(0, solveIdx).reverse();
			solveIdx = 0;
			nextState();
		}
	});

	$('#prev_state').click(function() {
		if (solveIdx > 0) {
			solveIdx = solveIdx - 1
			moves.push(solveMoves_rev[solveIdx])
			nextState()
		}
	});

	$('#next_state').click(function() {
		if (solveIdx < solveMoves.length) {
			moves.push(solveMoves[solveIdx])
			solveIdx = solveIdx + 1
			nextState()
		}
	});

	$('#last_state').click(function() {
		if (solveIdx < solveMoves.length) {
			moves = solveMoves.slice(solveIdx, solveMoves.length);
			solveIdx = solveMoves.length
			nextState();
		}
	});
	
	$('#string_state').click(function() {
		stringInput()
	});

	$('#cube_div').on("mousedown", function(ev) {
		lastMouseX = ev.clientX;
		lastMouseY = ev.clientY;
		$('#cube_div').on("mousemove", mouseMoved);
	});
	$('#cube_div').on("mouseup", function() {
		$('#cube_div').off("mousemove", mouseMoved);
	});
	$('#cube_div').on("mouseleave", function() {
		$('#cube_div').off("mousemove", mouseMoved);
	});

	console.log( "ready!" );
}));


function mouseMoved(ev) {
  var deltaX = ev.pageX - lastMouseX;
  var deltaY = ev.pageY - lastMouseY;

  lastMouseX = ev.pageX;
  lastMouseY = ev.pageY;

  rotY += deltaX * 0.2;
  rotX -= deltaY * 0.5;

  $("#cube").css("transform", "translateZ( -100px) rotateX( " + rotX + "deg) rotateY(" + rotY + "deg)");
}

