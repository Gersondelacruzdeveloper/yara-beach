// Set a user-friendly date
function setDate() {
    const dateElement = document.getElementById("date");
    
    if (dateElement) {
        const date = new Date(2024, 9, 17); // October 17, 2024 (months are 0-indexed in JavaScript)
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        dateElement.textContent = date.toLocaleDateString(undefined, options);
    }
}

// Timer settings
let time = 29 * 60 + 22; // 29 minutes and 22 seconds

// Function to format time as MM:SS
function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    return `${String(minutes).padStart(2, '0')}:${String(remainingSeconds).padStart(2, '0')}`;
}

// Update timer every second
function startTimer() {
    const timeSpan = document.getElementById("time");

    if (timeSpan) {
        const interval = setInterval(() => {
            if (time > 0) {
                time--;
                timeSpan.textContent = formatTime(time); // Update only the time part
            } else {
                clearInterval(interval);
                const timerElement = document.getElementById("timer");
                if (timerElement) {
                    timerElement.textContent = "Your hold has expired";
                }
            }
        }, 1000);
    }
}

// Start the timer and set the date on page load
window.onload = function() {
    setDate();
    startTimer();
};
