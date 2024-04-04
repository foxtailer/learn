const swiper = new Swiper('.top__swiper', {
  // Optional parameters
  //direction: 'vertical',
  loop: true,

  // autoplay: {
  //   delay: 3000,
  //   disableOnINteraction: false,
  // },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});

var swiper2 = new Swiper(".about__slider", {
  slidesPerView: 4,
  spaceBetween: 20,
  freeMode: true,
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});