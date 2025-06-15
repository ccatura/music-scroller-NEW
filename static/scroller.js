var playButton = document.getElementById("play-button");
var playButtonIcon = document.getElementById("play-button-icon");
var pauseButtonIcon = document.getElementById("pause-button-icon");

var slowerButton = document.getElementById('slower-button');
var fasterButton = document.getElementById('faster-button');
var scrollSpeedElement = document.getElementById("scroll-speed");
var scrollSpeedPreset = scrollSpeedElement.innerText;

var smallerButton = document.getElementById('smaller-button');
var largerButton = document.getElementById('larger-button');
var lyricsSizeElement = document.getElementById("lyrics-size");
var lyricsSizePreset = lyricsSizeElement.innerText;
var lyricsSizeIncrement = 5;
var lyricsSizeMax = 90;
var lyricsSizeMin = 10;
var lyrics = document.getElementById("lyrics");

var isScrolling = false;
var scroller;
var speedPresets = {
        12: 6,
        11: 8,
        10: 12,
        9:  15,
        8:  20,
        7:  30,
        6:  40,
        5:  60,
        4:  80,
        3:  100,
        2:  150,
        1:  100
    };
var topSpeed = Object.keys(speedPresets).length;
var speed = speedPresets[scrollSpeedPreset];

updateDisplays();

// Set the initial state of the play/pause button
playButton.addEventListener("click", function() {
    pauseButtonIcon.classList.toggle("hidden-div");
    if (isScrolling) {
        isScrolling = false;
        clearInterval(scroller);
    } else {
        isScrolling = true;
        scroll();
    }
    updateDisplays()
})

// Lowers the initial scroller speed
slowerButton.addEventListener("click", function() {
    if (scrollSpeedPreset > 1) {
        scrollSpeedPreset--;
        speed = speedPresets[scrollSpeedPreset];
        if(isScrolling) scroll();
    }
    updateDisplays();
})

// Increased the initial scroller speed
fasterButton.addEventListener("click", function() {
    if (scrollSpeedPreset < topSpeed) {
        scrollSpeedPreset++;
        speed = speedPresets[scrollSpeedPreset];
        if(isScrolling) scroll();
    }
    updateDisplays();
})

// Lowers the initial lyrics size
smallerButton.addEventListener("click", function() {
    if (lyricsSizePreset > lyricsSizeMin) {
        lyricsSizePreset = parseInt(lyricsSizePreset) - parseInt(lyricsSizeIncrement);
    }
    updateDisplays();
})

// Increases the initial lyrics size
largerButton.addEventListener("click", function() {
    if (lyricsSizePreset < lyricsSizeMax) {
        lyricsSizePreset = parseInt(lyricsSizePreset) + parseInt(lyricsSizeIncrement);
    }
    updateDisplays();
})

// Starts the scrolling effect
function scroll() {
    clearInterval(scroller);
    scroller = setInterval(() => {
        window.scrollBy(0, 1);
    }, speed);
}

// Detect when scrolled to bottom of page and stop
window.onscroll = function(ev) {
    if ((window.innerHeight + window.pageYOffset) >= document.body.offsetHeight) {
        isScrolling = false;
        clearInterval(scroller);
    }
    updateDisplays();
}

function updateDisplays() {
    console.log("isScrolling: " + isScrolling);
    console.log("scrollSpeedPreset: " + scrollSpeedPreset);
    console.log("lyricsSize: " + lyricsSizePreset);
    scrollSpeedElement.innerText = scrollSpeedPreset;
    lyricsSizeElement.innerText = lyricsSizePreset;
    lyrics.style.fontSize = lyricsSizePreset + "px";
    if (isScrolling) {
        playButtonIcon.classList.add("hidden-div");
        pauseButtonIcon.classList.remove("hidden-div");
    } else {
        playButtonIcon.classList.remove("hidden-div");
        pauseButtonIcon.classList.add("hidden-div");
    }
        console.log("\n");
}