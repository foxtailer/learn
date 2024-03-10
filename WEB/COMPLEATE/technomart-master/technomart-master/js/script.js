var basket = [];
var bookmarks = [];

var bookmarkField = document.getElementById('bookmark');
var bookmarkInfo = document.querySelector('.top-line__button--bookmark');

var basketField = document.getElementById('basket');
var basketInfo = document.querySelector('.top-line__button--basket');

var bookmarkButtons = document.querySelectorAll('.products__button--bookmark');

for (var i = 0; i < bookmarkButtons.length; i++) {
  bookmarkButtons[i].addEventListener('click', function (e) {
    e.preventDefault();
    var productId = e.target.dataset.productId;
    if (bookmarks.length > 50 || bookmarks.indexOf(productId) > -1) return;

    bookmarks.push(productId);
    bookmarkField.textContent = bookmarks.length;
    bookmarks.length && bookmarkInfo.classList.add('top-line__button--filled');
  });
}

// popups
var buyButtons = document.querySelectorAll('.products__button--buy');
var mapLink = document.querySelector('.about-us__link');

var basketPopup = document.querySelector('.modal--basket');
var mapPopup = document.querySelector('.modal--map');

var closePopupButtons = document.querySelectorAll('.modal__close');
var continueButton = document.querySelector('.button--continue');

for (var i = 0; i < buyButtons.length; i++) {
  buyButtons[i].addEventListener('click', function (e) {
    e.preventDefault();
    basketPopup.classList.add('modal--show');

    var productId = e.target.dataset.productId;
    if (basket.length > 50 || basket.indexOf(productId) > -1) return;

    basket.push(productId);
    basketField.textContent = basket.length;
    basket.length && basketInfo.classList.add('top-line__button--filled');
  });
}

mapLink && mapLink.addEventListener('click', function (e) {
  e.preventDefault();
  mapPopup.classList.add('modal--show');
});

continueButton.addEventListener('click', function (e) {
  e.preventDefault();
  basketPopup.classList.remove('modal--show');
});

for (var i = 0; i < closePopupButtons.length; i++) {
  closePopupButtons[i].addEventListener('click', function () {
    document.querySelector('.modal--show').classList.remove('modal--show');
  });
}

window.addEventListener('keydown', function (e) {
  if (e.keyCode === 27 && document.querySelector('.modal--show')) {
    e.preventDefault();
    document.querySelector('.modal--show').classList.remove('modal--show');
  }
});

// feedback form
var isStorageSupport = true;
var feedbackButton = document.querySelector('.button--feedback');
var feedbackPopup = document.querySelector('.modal--feedback');
var form = document.querySelector('.modal__form');
var fullName = document.querySelector('[name=name]');
var email = document.querySelector('[name=email]');
var message = document.querySelector('[name=message]');

try {
  storage = localStorage.getItem('name');
} catch (err) {
  isStorageSupport = false;
}

if (form) {
  form.addEventListener('change', function (e) {
    return isStorageSupport && localStorage.setItem(e.target.name, e.target.value)
  });
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    feedbackPopup.classList.remove("modal__error");
    if (!fullName.value || !email.value || !message.value) {
      feedbackPopup.offsetWidth = feedbackPopup.offsetWidth;
      feedbackPopup.classList.add("modal__error");
      return;
    }
    feedbackPopup.classList.remove("modal__error");
    feedbackPopup.classList.add("modal__success");
    setTimeout(function() {
      feedbackPopup.classList.remove("modal--show");
      feedbackPopup.classList.remove("modal__success");

      if (!isStorageSupport) {
        fullName.value = '';
        email.value = '';
        message.value = '';
      }
    }, 600);
    isStorageSupport && localStorage.clear();
  });
}

feedbackButton && feedbackButton.addEventListener('click', function (e) {
  e.preventDefault();
  feedbackPopup.classList.add('modal--show');

  if (isStorageSupport) {
    fullName.value = localStorage.getItem('name') || '';
    email.value = localStorage.getItem('email') || '';
    message.value = localStorage.getItem('message') || '';
  }
  fullName.focus();
});
// catalog slider
var catalogSlides = document.querySelectorAll('.catalog-slider__slide');
var prevSlideButton = document.querySelector('.catalog-slider__control');
var nextSlideButton = document.querySelector('.catalog-slider__control--next');
var catalogTabs = document.querySelectorAll('.catalog-slider__tab');

if (catalogSlides.length) {
  var currentCatalogSlideId = 0;

  var switchToNextSlide = function (id) {
    document.querySelector('.catalog-slider__slide--active').classList.remove('catalog-slider__slide--active');
    document.querySelector('.catalog-slider__tab--active').classList.remove('catalog-slider__tab--active');

    currentCatalogSlideId = id >= 0 ? id % catalogSlides.length : catalogSlides.length - 1;

    catalogSlides[currentCatalogSlideId].classList.add('catalog-slider__slide--active');
    catalogTabs[currentCatalogSlideId].classList.add('catalog-slider__tab--active');
  }

  for (var i = 0; i < catalogTabs.length; i++) {
    catalogTabs[i].addEventListener('click', function (e) {
      switchToNextSlide(e.target.dataset.slide);
    })
  }
  nextSlideButton.addEventListener('click', function () {
    switchToNextSlide(currentCatalogSlideId + 1);
  });
  prevSlideButton.addEventListener('click', function () {
    switchToNextSlide(currentCatalogSlideId - 1)
  });
}

// services slider
var serviceSlides = document.querySelectorAll('.services-slider__slide');
var serviceTabs = document.querySelectorAll('.services-slider__slide-button');

if (serviceSlides.length) {
  for (var i = 0; i < serviceTabs.length; i++) {
    serviceTabs[i].addEventListener('click', function (e) {
      document.querySelector('.services-slider__slide--active').classList.remove('services-slider__slide--active');
      document.querySelector('.services-slider__slide-button--active').classList.remove('services-slider__slide-button--active');

      serviceSlides[e.target.dataset.slide].classList.add('services-slider__slide--active');
      serviceTabs[e.target.dataset.slide].classList.add('services-slider__slide-button--active');
    })
  }
}
