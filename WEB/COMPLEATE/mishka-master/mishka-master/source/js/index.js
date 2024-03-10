'use strict';

svg4everybody(); // eslint-disable-line

(function() {
  // Меню
  const toggleButton = document.getElementById('toggle-button');
  const mainNav = document.querySelector('.main-nav');
  const siteNavigation = document.querySelector('.site-navigation');
  const userNavigation = document.querySelector('.user-navigation');

  if (mainNav && mainNav.classList.contains('main-nav--no-js')) {
    mainNav.classList.remove('main-nav--no-js');

    if (siteNavigation && userNavigation) {
      siteNavigation.classList.add('site-navigation--closed');
      userNavigation.classList.add('user-navigation--closed');
    }
  }

  if (toggleButton) {
    toggleButton.addEventListener('click', function(event) {
      event.preventDefault();
      siteNavigation.classList.toggle('site-navigation--closed');
      userNavigation.classList.toggle('user-navigation--closed');
      this.classList.toggle('main-nav__toggle--off');
    });
  }

  // Модальное окно заказа товара
  const overlayModal = document.querySelector('.modal-overlay');
  const catalogBlock = document.querySelector('.catalog');
  const orderButton = document.querySelector('.week-goods__button');

  if (overlayModal) {
    if (catalogBlock) {
      catalogBlock.addEventListener('click', openOrderForm);
    }

    if (orderButton) {
      orderButton.addEventListener('click', openOrderForm);
    }

    overlayModal.addEventListener('click', closeOrderForm);
    window.addEventListener('keydown', closeOrderForm);
  }

  function openOrderForm(event) {
    let element = event.target;

    if (
      element.classList.contains('card-product__button') ||
      element.classList.contains('week-goods__button')
    ) {
      event.preventDefault();
      overlayModal.classList.add('modal-overlay--opened');
    }
  }

  function closeOrderForm(event) {
    let element = event.target;

    if (element.classList.contains('modal-overlay') || event.keyCode === 27) {
      overlayModal.classList.remove('modal-overlay--opened');
    }
  }
})();

// Яндекс карта
/*eslint-disable*/
function init(ymaps) {
  /*eslint-enable*/
  let map = new ymaps.Map('map', {
    center: [59.93944115603922, 30.32302403991186],
    zoom: 16,
    controls: ['zoomControl']
  });

  let placemark = new ymaps.Placemark(
    [59.938633647616214, 30.32304549758399],
    {},
    {
      iconLayout: 'default#image',
      iconImageHref: 'img/icon-map-pin.svg',
      iconImageSize: [66, 101],
      iconImageOffset: [-33, -101]
    }
  );

  map.behaviors.disable('scrollZoom');
  map.geoObjects.add(placemark);
}
