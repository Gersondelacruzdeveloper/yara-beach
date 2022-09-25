

// Variables for slide in home
let slide = document.getElementsByClassName("slide")
let heading = document.getElementsByClassName("heading")
// Variables detail page
let thumbnails = document.getElementsByClassName('thumbnails')
let activeImages = document.getElementsByClassName('active-image')
let expandedImg = document.getElementById('expandedImg')
let arrowLeft = document.getElementById('arrow-left');
let arrowRight = document.getElementById('arrow-right');

/**
 * 
 * @param {*} list take a list and add and remove an active class
 */

function slideShow(list) {
  for (let i = 0; i < list.length; i++) {
    let index = 1
    list[index].classList.add('active')
    setInterval(() => {
      list[index].classList.remove('active')
      index++
      if (index === list.length) index = 0;
      list[index].classList.add('active');
    }, 5000);
  }
}

slideShow(slide)
slideShow(heading)



// detail page

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
