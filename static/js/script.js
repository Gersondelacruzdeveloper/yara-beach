
const slide = document.getElementsByClassName("slide")
const heading = document.getElementsByClassName("heading")

/**
 * 
 * @param {*} list take a list and add and remove an active class
 */
const slideShow =(list)=>{
  for(let i in list){
    let index = 1
    list[index].classList.add('active')
    setInterval(()=>{
      list[index].classList.remove('active')
      index++
      if(index === list.length) index = 0
      list[index].classList.add('active')
    }, 5000)
  }
}

// Call the slideShow function 
slideShow(slide)
slideShow(heading)

