
document.addEventListener('DOMContentLoaded', function() {
    const discountBadge = document.querySelector('.discount-badge');
    discountBadge.textContent = '20% OFF';

    const productCodeElement = document.querySelector('.product-code');
    productCodeElement.textContent = 'Product Code: del506';

    const countdownElement = document.getElementById('countdown');

    function updateCountdown() {
        const now = new Date();
        let startTime = localStorage.getItem('discountStartTime');

        if (!startTime) {
            // If the start time is not set, set it to the current time
            startTime = now.getTime();
            localStorage.setItem('discountStartTime', startTime);
        } else {
            startTime = parseInt(startTime, 10);
        }

        const endTime = new Date(startTime + 24 * 60 * 60 * 1000); // 24 hours in milliseconds
        const timeLeft = endTime - now;

        if (timeLeft <= 0) {
            // If 24 hours have passed, reset the countdown and update the start time
            startTime = now.getTime();
            localStorage.setItem('discountStartTime', startTime);
        }

        const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

        countdownElement.textContent = `Offer ends in: ${days}d ${hours}h ${minutes}m ${seconds}s`;
    }

    // Update the countdown every second
    setInterval(updateCountdown, 1000);
    updateCountdown();
});