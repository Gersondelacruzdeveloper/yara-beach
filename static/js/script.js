
// Variables detail page
let thumbnails = document.getElementsByClassName('thumbnails')
let activeImages = document.getElementsByClassName('active-image')
let expandedImg = document.getElementById('expandedImg')
let arrowLeft = document.getElementById('arrow-left');
let arrowRight = document.getElementById('arrow-right');
// Variables edit page
let upload_img = document.getElementById('id_images')


// -----------------------------------------------------------detail page

//Add event listener to all thumbnails
for (let i = 0; i < thumbnails.length; i++) {
  thumbnails[i].addEventListener('click', switchImages)
}

/**
 * Switch Images and add and remove active-image class
 */
function switchImages() {
  expandedImg.src = this.src;
  if (activeImages.length > 0) {
    activeImages[0].classList.remove('active-image')
  }
  this.classList.add('active-image')
}

// When click on the left arrow the allphotos div will scroll -50
if (arrowLeft) {
  arrowLeft.addEventListener('click', function () {
    document.getElementById('allphotos').scrollLeft -= 50
  })
}

// When click on the right arrow the allphotos div will scroll + 50
if (arrowRight) {
  arrowRight.addEventListener('click', function () {
    document.getElementById('allphotos').scrollLeft += 50
  })
}

// -------------------------------------------------------------  Edit page
// Make it posible to add multiple images
if(upload_img){
  // add multiple image
  upload_img.setAttribute("multiple", "")
  // Remove require atribute in order to allow reverse back with no issues
  upload_img.removeAttribute('required')
}