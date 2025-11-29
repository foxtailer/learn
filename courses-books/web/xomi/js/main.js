let slideIndex = 0;
let slideIndexBot = 0;
showSlides();
showSlidesBot();

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("slider__item");
  let dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }

  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "block";

  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" dot__active", "");
  }
  dots[slideIndex-1].className += " dot__active";

  setTimeout(showSlides, 2000);
};

function currentSlide(n) {
    slideIndex = n;
  }


function showSlidesBot() {
  let i;
  let slides = document.getElementsByClassName("slider__item-bottom");
  let dots = document.getElementsByClassName("dot-bottom");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }

  slideIndexBot++;
  if (slideIndexBot > slides.length) {slideIndexBot = 1}
  slides[slideIndexBot-1].style.display = "block";

  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" dot__active", "");
  }

  dots[slideIndexBot-1].className += " dot__active";

  setTimeout(showSlidesBot, 2000);
};
  

// function showSlides() {
//   let i;
//   let slides = document.getElementsByClassName("slider__item");
//   for (i = 0; i < slides.length; i++) {
//     setSlides(i)
//   }
//   slideIndex++;
//   if (slideIndex > slides.length) {slideIndex = 1}
//   slides[slideIndex-1].style.display = "block";
//   setTimeout(showSlides, 2000);
// }

// function currentSlide(n) {
//   setSlides(slideIndex = n);
// }

// function setSlides(n) {
//   let i;
//   let slides = document.getElementsByClassName("slider__item");
//   let dots = document.getElementsByClassName("dot");
//   if (n > slides.length) {slideIndex = 1}
//   if (n < 1) {slideIndex = slides.length}
//   for (i = 0; i < slides.length; i++) {
//     slides[i].style.display = "none";
//   }
//   for (i = 0; i < dots.length; i++) {
//     dots[i].className = dots[i].className.replace(" dot__active", "");
//   }
//   slides[slideIndex-1].style.display = "block";
//   dots[slideIndex-1].className += " dot__active";
// }