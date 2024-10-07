// Example: Simple scroll event to trigger animations
window.addEventListener("scroll", function () {
    const header = document.querySelector('.Hero-header ');
    const scrolled = window.scrollY;
    
    header.style.opacity = Math.max(1 - scrolled / 1000, 0.3);  // Ensures opacity doesn’t go below 0.3

});
