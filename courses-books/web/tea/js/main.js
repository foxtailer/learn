let menuBtn = document.querySelector(".menu__btn");
let menuCloseBtn = document.querySelector(".menu__close-btn")
let menu = document.querySelector(".menu__list")

menuBtn.addEventListener("click", () => {
  menu.classList.toggle("menu__list-show")
})
menuCloseBtn.addEventListener("click", () => {
  menu.classList.toggle("menu__list-show")
})