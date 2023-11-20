
// Variables edit page
let upload_img = document.getElementById('id_images')

// -----------------------------------------------------------detail page
let thumbnails = document.getElementsByClassName('thumbnails');
let activeImages = document.getElementsByClassName('active-image');
let expandedImg = document.getElementById('expandedImg');
let arrowLeft = document.getElementById('arrow-left');
let arrowRight = document.getElementById('arrow-right');

// Add event listener to all thumbnails
for (let i = 0; i < thumbnails.length; i++) {
  thumbnails[i].addEventListener('click', switchImages);
}

/**
 * Switch Images and add and remove active-image class
 */
function switchImages() {
  expandedImg.src = this.src;
  if (activeImages.length > 0) {
    activeImages[0].classList.remove('active-image');
  }
  this.classList.add('active-image');
}

// When click on the left arrow, scroll and switch to the previous image
if (arrowLeft) {
  arrowLeft.addEventListener('click', function () {
    document.getElementById('allphotos').scrollLeft -= 50;
    switchToPreviousImage();
  });
}

// When click on the right arrow, scroll and switch to the next image
if (arrowRight) {
  arrowRight.addEventListener('click', function () {
    document.getElementById('allphotos').scrollLeft += 50;
    switchToNextImage();
  });
}

// Function to switch to the previous image
function switchToPreviousImage() {
  let currentIndex = Array.from(thumbnails).indexOf(document.querySelector('.active-image'));
  let previousIndex = (currentIndex - 1 + thumbnails.length) % thumbnails.length;
  thumbnails[previousIndex].click();
}

// Function to switch to the next image
function switchToNextImage() {
  let currentIndex = Array.from(thumbnails).indexOf(document.querySelector('.active-image'));
  let nextIndex = (currentIndex + 1) % thumbnails.length;
  thumbnails[nextIndex].click();
}


// -------------------------------------------------------------  Edit page
// Make it posible to add multiple images
if(upload_img){
  // add multiple image
  upload_img.setAttribute("multiple", "")
  // Remove require atribute in order to allow reverse back with no issues
  upload_img.removeAttribute('required')
}