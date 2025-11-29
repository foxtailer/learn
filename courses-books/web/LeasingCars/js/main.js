

const tabItem = document.querySelectorAll('.tabs-btns-item');
const tabContent = document.querySelectorAll('.tabs-content');

tabItem.forEach(function(element) {
  element.addEventListener("click", open);
});

function open(evt){
  const tabTarget = evt.currentTarget;
  const button = tabTarget.dataset.button;

  tabItem.forEach(function(item){
    item.classList.remove("tabs-btns-item-actine");
  })

  tabTarget.classList.add("tabs-btns-item-actine");

  tabContent.forEach(function(item){
    item.classList.remove("tabs-content-active");
  });

  document.querySelector(`#${button}`).classList.add("tabs-content-active")
}

var swiper = new Swiper(".swiper", {
  effect: "fade",
  pagination: {
    el: ".swiper-pagination",
  },
  autoplay: {
    delay: 2000,
    disableOnInteraction: false,
  }
});