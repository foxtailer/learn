let slideIndex = 0;
let slides = document.getElementsByClassName("slider-content__img");
showSlide();

function showSlide() {
  document.getElementById("img-index-max").innerHTML = "0" + (slides.length-1);
  slides[slideIndex].style.display = "block";
};

function moveSlide(direction) {
  let left = document.getElementById("slider__left");
  let right = document.getElementById("slider__right");

  if (direction=="-" && slideIndex>0) {slides[slideIndex].style.display = "none"; slideIndex--;}
  if (direction=="+" && slideIndex<slides.length-2) {slides[slideIndex].style.display = "none"; slideIndex++}
  
  slides[slideIndex].style.display = "block";
  document.getElementById("img-index-current--last").innerHTML = slideIndex+1

  if (slideIndex > 0) {left.classList.add("slider__btn--evailable")} else 
  {left.classList.remove("slider__btn--evailable")} 

  if (slideIndex == slides.length-2) {right.classList.remove("slider__btn--evailable")} else 
  {right.classList.add("slider__btn--evailable")} 
}