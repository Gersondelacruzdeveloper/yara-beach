document.addEventListener("DOMContentLoaded", function() {
    const images = document.querySelectorAll('.gallery img');
    const fullscreen = document.getElementById('fullscreen');
    const fullscreenImg = document.getElementById('fullscreen-img');
    const counter = document.getElementById('counter');
  
    let currentIndex = 0;
  
    // Ensure elements exist before adding event listeners
    if (images.length && fullscreen && fullscreenImg && counter) {
      images.forEach((img, index) => {
        img.addEventListener('click', () => {
          openFullscreen(index);
        });
      });
  
      function openFullscreen(index) {
        currentIndex = index;
        fullscreen.style.display = 'flex';
        fullscreenImg.src = images[currentIndex].src;
        updateCounter();
      }
  
      function updateCounter() {
        counter.textContent = `${currentIndex + 1} / ${images.length}`;
      }
      function closeFullscreen() {
        const fullscreen = document.getElementById('fullscreen');
        
        if (fullscreen) {
          fullscreen.style.display = 'none';
        } else {
          console.error("Fullscreen element not found in the DOM.");
        }
      }
  
      function nextImage() {
        currentIndex = (currentIndex + 1) % images.length;
        fullscreenImg.src = images[currentIndex].src;
        updateCounter();
      }
  
      function prevImage() {
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        fullscreenImg.src = images[currentIndex].src;
        updateCounter();
      }
  
      // Close fullscreen if user clicks outside the image
      fullscreen.addEventListener('click', (e) => {
        if (e.target === fullscreen) {
          closeFullscreen();
        }
      });
  
      // Expose nextImage and prevImage functions to global scope for next/prev controls
      window.nextImage = nextImage;
      window.prevImage = prevImage;
      window.closeFullscreen = closeFullscreen;
    } else {
      console.error("Required elements (images, fullscreen, or counter) are missing from the DOM.");
    }
  });
  