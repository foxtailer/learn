var pool = document.querySelector(".pool");
let template = document.querySelector('#item-template').content.querySelector('div');
let cells =  document.querySelectorAll('.cell')
let items = [];

function shufflePool() {
  // var items_arr = Array.from(items)
  // for (let i=0; i<items.length; i++){
  //   pool.removeChild(items[i])
  // }
  // for (let i=0; i<items.length; i++){
  //   let n = Math.floor(Math.random()*items_arr.length)
  //   pool.appendChild(items_arr[n])
  //   items_arr.splice(n,1)
  // }
  // Object.keys(pool).length === 0

  let temp = [0];
  
  pool.children[15].innerHTML = ""
  while (temp.length < 16){
    let n = Math.floor(Math.random()*16);

    if (!temp.includes(n)){ 
      let element = template.cloneNode(true);
      element.textContent = n;
      element.draggable = true;
      pool.children[temp.length-1].innerHTML = ""
      pool.children[temp.length-1].appendChild(element)

      temp.push(n);
    };    
  };

  items = document.querySelectorAll(".item");
  items.forEach(item => {
    item.addEventListener("dragstart", () => {
      item.classList.add("draging");
    })
    item.addEventListener("dragend", () => {
      item.classList.remove("draging");
    })
    
    let touchedElement
    item.addEventListener("touchmove", (e) => {
      e.preventDefault()
      var touchLocation = e.targetTouches[0];
      touchedElement = document.elementFromPoint(touchLocation.clientX, touchLocation.clientY);
      item.style.position = "absolute"
      item.style.width = "50px"
      item.style.height = "50px"
      item.style.left = touchLocation.pageX + 'px';
      item.style.top = touchLocation.pageY + 'px';
    });
    item.addEventListener("touchend", (e) => {
      e.preventDefault()
      item.style.position = "initial"
      item.style.width = ""
      item.style.height = ""
      const touchLocation = e.changedTouches[0];
      const targetElement = document.elementFromPoint(touchLocation.clientX, touchLocation.clientY);

      const sourceIndex = Array.from(cells).indexOf(touchedElement.parentElement)
      const targetIndex = Array.from(cells).indexOf(targetElement)
      const isAdjacent = Math.abs(targetIndex - sourceIndex) === 1 || Math.abs(targetIndex - sourceIndex) === 4;
      
      if (isAdjacent && targetElement.textContent === "") {
        targetElement.appendChild(touchedElement)
        manageCells();
      }
    });
  });
};


let emptyCell;
function manageCells() {
  cells.forEach(cell => {
    if (cell.textContent === "") {
      emptyCell = cell
      cell.addEventListener("dragover", e => {
        e.preventDefault();
      });
    }
  })
}

cells.forEach(cell => {
  cell.addEventListener("drop", e => {
    const draggedItem = document.querySelector(".draging");

    const targetCell = e.target.closest(".cell");
    const sourceCell = draggedItem.parentElement;

    // Check if the target cell is adjacent to the source cell
    const sourceIndex = Array.from(sourceCell.parentElement.children).indexOf(sourceCell);
    const targetIndex = Array.from(targetCell.parentElement.children).indexOf(targetCell);
    const isAdjacent = Math.abs(targetIndex - sourceIndex) === 1 || Math.abs(targetIndex - sourceIndex) === 4;

    if (isAdjacent && targetCell.textContent === "") {
      targetCell.appendChild(draggedItem); // Move the dragged item to the target cell
      manageCells();
      // emptyCells.push(sourceCell); // Add the source cell to the list of empty cells
      // emptyCells = emptyCells.filter(cell => cell !== targetCell); // Remove the target cell from the list of empty cells
    }
  }); 
})

manageCells();