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



// add to card functionality for customers
document.addEventListener("DOMContentLoaded", function() {
  let ticketCounts = { adult: 0, child: 0, infant: 0 };

  let adultPriceElement = document.getElementById("adult-price");
  let childrenPriceElement = document.getElementById("children-price");
  let infantPriceElement = document.getElementById("infant-price");

  let adultPrice = adultPriceElement ? parseFloat(adultPriceElement.textContent.replace(/[^\d.-]/g, '')) : 0;
  let childrenPrice = childrenPriceElement ? parseFloat(childrenPriceElement.textContent.replace(/[^\d.-]/g, '')) : 0;
  let infantPrice = infantPriceElement ? parseFloat(infantPriceElement.textContent.replace(/[^\d.-]/g, '')) : 0;

  let prices = { adult: adultPrice, child: childrenPrice, infant: infantPrice };

  function updateTicketCount(type, change) {
    ticketCounts[type] = Math.max(0, ticketCounts[type] + change);

    let countElement = document.getElementById(`${type}-count`);
    if (countElement) {
      countElement.value = ticketCounts[type];
    }

    updateTotal();
  }

  function updateTotal() {
    let total =
      ticketCounts.adult * prices.adult +
      ticketCounts.child * prices.child +
      ticketCounts.infant * prices.infant;

    let totalElement = document.getElementById("total");
    if (totalElement) {
      totalElement.textContent = total.toFixed(2);
    }
  }

  function attachInputListeners() {
    document.getElementById("adult-count").addEventListener("input", function () {
      let value = parseInt(this.value) || 0;
      ticketCounts.adult = value;
      updateTotal();
    });

    let childInput = document.getElementById("child-count");
    if (childInput) {
      childInput.addEventListener("input", function () {
        let value = parseInt(this.value) || 0;
        ticketCounts.child = value;
        updateTotal();
      });
    }

    let infantInput = document.getElementById("infant-count");
    if (infantInput) {
      infantInput.addEventListener("input", function () {
        let value = parseInt(this.value) || 0;
        ticketCounts.infant = value;
        updateTotal();
      });
    }
  }

  // Validate form submission
  document.querySelector("form").addEventListener("submit", function(event) {
    const adultCount = document.getElementById("adult-count").value;
    if (adultCount == 0) {
      event.preventDefault(); // Prevent form submission
      alert("Please select at least 1 adult ticket.");
      document.getElementById("adult-count").focus(); // Set focus on the input field
    }
  });

  attachInputListeners();

  window.updateTicketCount = updateTicketCount;
});
