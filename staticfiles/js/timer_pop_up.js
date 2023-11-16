
// Set the initial countdown time in seconds
let countdownSeconds = 30 * 60 + 18;

function updateTimer() {
    // Calculate minutes and seconds
    const minutes = Math.floor(countdownSeconds / 60);
    const seconds = countdownSeconds % 60;

    // Display the time in the "timer" div
    document.getElementById('timer').innerHTML = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;

    // Decrease the countdown time
    countdownSeconds--;

    // Restart the countdown when it reaches 0
    if (countdownSeconds < 0) {
        countdownSeconds = 18 * 60 + 18;
    }
}

// Update the timer every second
setInterval(updateTimer, 1000);

// Initial call to set up the timer display
updateTimer();
