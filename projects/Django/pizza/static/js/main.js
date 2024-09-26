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