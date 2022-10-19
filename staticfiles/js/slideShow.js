// Variables for slide in home
let slide = document.getElementsByClassName("slide")
let heading = document.getElementsByClassName("heading")

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
  