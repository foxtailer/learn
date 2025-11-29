const menuIcon = document.getElementById("menu-btn");
const lines = document.querySelectorAll(".no-animation");
let flag = 0

menuIcon.addEventListener("click", () => {
  menuIcon.classList.toggle("active");

  if (flag == 0) {
    document.getElementById("nav__inner").style.display = "flex";
    flag++
  } else {
    document.getElementById("nav__inner").style.display = "none";
    flag--
  }
  

  lines.forEach((line) => {
    line.classList.remove("no-animation");
  });
});
