// Example: Simple scroll event to trigger animations
window.addEventListener("scroll", function () {
    const header = document.querySelector('.Hero-header ');
    const scrolled = window.scrollY;
    
    header.style.opacity = 1 - scrolled / 500;  // Fades out header image as you scroll
});
