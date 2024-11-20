const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

// Dropdown language and location buttons
function langDropdown() {
  document.getElementById("lang-dropdown").classList.toggle("show");
}

function locationDropdown() {
  document.getElementById("location-dropdown").classList.toggle("show");
}

function changeLocation(locationName) {
  document.getElementById('location-btn').innerHTML = locationName;
  document.getElementById('location-dropdown').classList.remove('show');
}

function changeLanguage(languageName) {
  document.getElementById('lang-btn').innerHTML = languageName;
  document.getElementById('lang-dropdown').classList.remove('show');
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.drop-btn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}


// Menu btn hide and animation
const menuIcon = document.getElementById("menu-btn");
const lines = document.querySelectorAll(".no-animation")
let navigation = document.querySelector(".main-nav__list")

menuIcon.addEventListener("click", ()=> {
  menuIcon.classList.toggle("active");
  navigation.classList.toggle("active");

  lines.forEach((line) => {
    line.classList.remove("no-animation");
  });
});

window.onscroll = () => {
  menuIcon.classList.remove("active");
  navigation.classList.remove("active");

  lines.forEach((line) => {
    line.classList.remove("no-animation");
  });
}


// Ingrediens
const boxes = document.querySelectorAll('.card-image');

boxes.forEach(box => {
  const card = box.closest('.card');
  
  const hiddenContent = card.querySelector('.ingredients-control');
  
  if (hiddenContent) {
    box.addEventListener('mouseenter', function() {
      hiddenContent.classList.remove('hidden');
    });

    box.addEventListener('mouseleave', function() {
      if (!hiddenContent.matches(':hover')) {
        hiddenContent.classList.add('hidden');
      }
    });

    hiddenContent.addEventListener('mouseenter', function() {
      hiddenContent.classList.remove('hidden');
    });

    hiddenContent.addEventListener('mouseleave', function() {
      hiddenContent.classList.add('hidden');
    });
  }
});


// Quantity/Size control
document.addEventListener('DOMContentLoaded', function () {
  const quantityControls = document.querySelectorAll('.quantity-control');
  const sizeControls = document.querySelectorAll('.size-control input[type="radio"]'); // All size radio buttons

  const minValue = 1;
  const maxValue = 100;

  // Function to update the price based on the selected size (Small, Medium, Large)
  function updatePriceBasedOnSize(card, selectedSize) {
    const price = card.querySelector('.price');
    const basePrice = parseFloat(price.dataset.unitPrice); // Base price of the product

    // Determine the multiplier for the selected size
    let sizeMultiplier = 1; // Default to 100% (Medium)
    
    if (selectedSize === 'S') {
      sizeMultiplier = 0.8; // Small = 80%
    } else if (selectedSize === 'L') {
      sizeMultiplier = 1.2; // Large = 120%
    }

    // Adjust the price based on the selected size
    const adjustedPrice = basePrice * sizeMultiplier;
    
    // Update the price in the card's .price element
    price.dataset.adjustedPrice = adjustedPrice;  // Store the adjusted price for use with quantity
    price.innerHTML = `$ ${adjustedPrice.toFixed(2)}`;  // Update the displayed price
  }

  // Event listener for size changes
  sizeControls.forEach(function (radio) {
    radio.addEventListener('change', function () {
      const card = radio.closest('.card');
      const selectedSize = radio.value; // Get the selected size (S, M, L)
      updatePriceBasedOnSize(card, selectedSize);
      
      // Recalculate the price based on the selected size and quantity
      const inputField = card.querySelector('.quantity-control__input');
      const currentQuantity = parseInt(inputField.value, 10);
      const price = card.querySelector('.price');
      const adjustedPrice = parseFloat(price.dataset.adjustedPrice); // Get the adjusted price
      const finalPrice = adjustedPrice * currentQuantity;
      price.innerHTML = `$ ${finalPrice.toFixed(2)}`; // Update the price based on quantity
    });
  });

  // Function to update the price based on quantity
  function updateValue(inputField, newValue, price) {
    const adjustedPrice = parseFloat(price.dataset.adjustedPrice); // Get the adjusted price
    const finalPrice = adjustedPrice * newValue;  // Calculate price based on quantity
    price.innerHTML = `$ ${finalPrice.toFixed(2)}`;  // Update price based on quantity
    inputField.value = newValue;  // Update the input value to the new quantity
  }

  quantityControls.forEach(function (control) {
    const inputField = control.querySelector('.quantity-control__input');
    const decrementButton = control.querySelector('.decrement');
    const incrementButton = control.querySelector('.increment');
    const card = control.closest('.card'); // Find the closest parent .card
    const price = card.querySelector('.price'); // Find the .price within the same card
    const basePrice = parseFloat(price.dataset.unitPrice); // Get the base price from data

    // Make sure that the price element has a data attribute for unit price
    if (!price.dataset.unitPrice) {
      // If the price data is not available, fetch it from the product price element
      price.dataset.unitPrice = price.innerHTML.replace('$', '').trim();
    }

    // Initially set the adjusted price based on the default size (Medium, or based on initial selection)
    const initialSize = card.querySelector('input[name="size"]:checked').value;
    updatePriceBasedOnSize(card, initialSize);

    decrementButton.addEventListener('click', function () {
      let currentValue = parseInt(inputField.value, 10);
      if (currentValue > minValue) {
        currentValue--;
        updateValue(inputField, currentValue, price);
      }
    });

    incrementButton.addEventListener('click', function () {
      let currentValue = parseInt(inputField.value, 10);
      if (currentValue < maxValue) {
        currentValue++;
        updateValue(inputField, currentValue, price);
      }
    });
  });
});


// Rating stars
const ratings = document.querySelectorAll('.rating');
if (ratings.length > 0) {
  initRatings();
}

function initRatings() {
  let ratingActive, ratingValue;

  for (let index = 0; index < ratings.length; index++) {
    const rating = ratings[index];
    initRating(rating)
  }

  function initRating(rating) {
    initRatingVars(rating);
    setRatingActiveWidth();

    if (rating.classList.contains('rating_set')) {
      setRating(rating);
    }
  }

  function initRatingVars(rating) {
    ratingActive = rating.querySelector('.rating__active'); 
    ratingValue = rating.querySelector('.rating__value'); 
  }

  function setRatingActiveWidth(index = ratingValue.innerHTML) {
    const ratingActiveWidth = index / 0.05;
    ratingActive.style.width = `${ratingActiveWidth}%`; 
  }

  function setRating(rating) {
    const ratingItems = rating.querySelectorAll('.rating__item');
    for (let index = 0; index < ratingItems.length;  index++) {
      const ratingItem = ratingItems[index];

      ratingItem.addEventListener('mouseenter', function (e) {
        initRatingVars(rating);
        setRatingActiveWidth(ratingItem.value);
      });
      ratingItem.addEventListener('mouseleave', function (e) {
        setRatingActiveWidth();
      });
      ratingItem.addEventListener('click', function (e) {
        initRatingVars(rating);

        if (rating.dataset.ajax) {
          setRatingValue(ratingItem.value, rating);
        } //else {
        //   ratingValue.innerHTML = index + 1;
        //   setRatingActiveWidth();
        // }
      });
    }
  }

  async function setRatingValue(value, rating) {
    if (!rating.classList.contains('rating_sending')) {
      rating.classList.add('rating_sending');

      const productId = rating.dataset.productId;

      let response = await fetch('/update-rating/', {
        method: 'POST',

        body: JSON.stringify({
          userRating: value,
          productId: productId,
        }),
        
        headers: {
          'content-type': 'application/json',
          'X-CSRFToken': csrfToken,
        }
      });
      if (response.ok) {
        const result = await response.json();

        const newRating = result.newRating;

        ratingValue.innerHTML = newRating;

        setRatingActiveWidth();
        rating.classList.remove('rating_sending');
      } else {
        alert('Error');
        rating.classList.remove('rating_sending');
      }
    }
  }
}


// Cart show
var popup = document.querySelector(".global-cart")
var close = document.querySelector(".cart-close")
var open = document.querySelector(".order-btn")

open.addEventListener("click", function(evt){
    if (!popup.classList.contains("modal-show")) {
        popup.classList.add("modal-show");
    }
});


close.addEventListener("click", function(evt){
  popup.classList.toggle("modal-show");
});


//TODO
{/* <input type="password" id="password" />
<button id="togglePassword">Show</button>

<script>
  const togglePassword = document.getElementById('togglePassword');
  const passwordInput = document.getElementById('password');

  togglePassword.addEventListener('click', () => {
    // Toggle the input type
    const type = passwordInput.type === 'password' ? 'text' : 'password';
    passwordInput.type = type;

    // Optional: change the button text
    togglePassword.textContent = type === 'password' ? 'Show' : 'Hide';
  });
</script> */}
