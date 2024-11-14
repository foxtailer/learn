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


// Get all elements with class 'card-image'
const boxes = document.querySelectorAll('.card-image');

// Loop through each 'card-image' element
boxes.forEach(box => {
  // Find the parent card element (the card that contains both the image and the ingredients control)
  const card = box.closest('.card');
  
  // Try to find the associated ingredients control within the card
  const hiddenContent = card.querySelector('.ingredients-control');
  
  // If the ingredients control exists, add the event listeners
  if (hiddenContent) {
    // Add event listener for mouse enter (hover) to show the ingredients control
    box.addEventListener('mouseenter', function() {
      hiddenContent.classList.remove('hidden');  // Show the ingredients control
    });

    // Add event listener for mouse leave on the image
    box.addEventListener('mouseleave', function() {
      // Only hide ingredients if the mouse is not over the ingredients control
      if (!hiddenContent.matches(':hover')) {
        hiddenContent.classList.add('hidden');  // Hide the ingredients control
      }
    });

    // Add event listener for mouse enter on the ingredients control (to keep it visible)
    hiddenContent.addEventListener('mouseenter', function() {
      hiddenContent.classList.remove('hidden');  // Keep the ingredients control visible
    });

    // Add event listener for mouse leave on the ingredients control (to hide it again)
    hiddenContent.addEventListener('mouseleave', function() {
      hiddenContent.classList.add('hidden');  // Hide the ingredients control when mouse leaves
    });
  }
});


document.addEventListener('DOMContentLoaded', function () {
  // Get all elements with class 'quantity-control'
  const quantityControls = document.querySelectorAll('.quantity-control');

  // Set initial values
  const minValue = 1;  // Minimum allowed value for the input
  const maxValue = 100; // Maximum allowed value for the input (optional, can be adjusted)

  // Function to update the input value for each quantity control
  function updateValue(inputField, newValue) {
    // Ensure the value is within bounds (minValue and maxValue)
    if (newValue >= minValue && newValue <= maxValue) {
      inputField.value = newValue;
    }
  }

  // Loop through each quantity control and add event listeners to its buttons
  quantityControls.forEach(function (control) {
    const inputField = control.querySelector('.quantity-control__input');
    const decrementButton = control.querySelector('.decrement');
    const incrementButton = control.querySelector('.increment');

    // Event listener for the decrement button
    decrementButton.addEventListener('click', function() {
      let currentValue = parseInt(inputField.value, 10);
      if (currentValue > minValue) {
        currentValue--;
        updateValue(inputField, currentValue);
      }
    });

    // Event listener for the increment button
    incrementButton.addEventListener('click', function() {
      let currentValue = parseInt(inputField.value, 10);
      if (currentValue < maxValue) {
        currentValue++;
        updateValue(inputField, currentValue);
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
