let container = document.querySelector(".img-container");
let score = document.querySelector(".score");
let flagList = Object.keys(data);
import data from './flags_short.json' assert { type: 'json' };
let answ = 0;
let questions = 0;
let trueAnswer;
let trueBtn;

function setFlag() {
  let i = Math.floor(Math.random()*270);
  let item = data[flagList[i]];
  container.innerHTML = item["1x1"];
  trueAnswer = item["name"];
};

function setButtons(trueAnswer) {
  let i = Math.floor(Math.random()*4);
  let buttons = document.querySelectorAll(".button");
  buttons[i].textContent = trueAnswer;
  score.textContent = answ + "/" + questions;
  
  let asignFalse = 0;
  let awailableBtns = [0, 1, 2, 3]
  awailableBtns.splice(i, 1);

  while(asignFalse < 3){
    let j = Math.floor(Math.random()*270);
    let falseAnswer = data[flagList[j]]["name"];

    if (falseAnswer !== trueAnswer){
      buttons[awailableBtns[asignFalse]].textContent = falseAnswer;
      asignFalse++;
    }
  }

  trueBtn = i;
};

document.querySelector("#btn-1").addEventListener("click", ()=> {
  if (0 == trueBtn){
    answ++;
    reSet();
  }
  else {
    reSet();
  }
});
document.querySelector("#btn-2").addEventListener("click", ()=> {
  if (1 == trueBtn){
    answ++;
    reSet();
  }
  else {
    reSet();
  }
});
document.querySelector("#btn-3").addEventListener("click", ()=> {
  if (2 == trueBtn){
    answ++;
    reSet();
  }
  else {
    reSet();
  }
});
document.querySelector("#btn-4").addEventListener("click", ()=> {
  if (3 == trueBtn){
    answ++;
    reSet();
  }
  else {
    reSet();
  }
});

function reSet() {
  questions++;
  setFlag();
  setButtons(trueAnswer);
  console.log(trueBtn);
};

//console.log(Object.keys(data).length);
//console.log(typeof Object.keys(data).length);
setFlag();
setButtons(trueAnswer);
console.log(trueBtn);