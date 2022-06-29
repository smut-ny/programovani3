const DEFAULT_OPTIONS = {
    isRandomSeed: true

}

export default class GameLogic {
    #CanvasSelector = '#canvas'
    #LastRowSelector = '.row:last-child' 

    constructor(options) {
        Object.entries({ ...DEFAULT_OPTIONS, ...options }).forEach(([key, value]) => {
            this[key] = value;
        })
    }

    startGame(){
        // Init map
        this.render(this.isRandomSeed, true);

        // Steps
        setInterval(e => {
            this.renderSteps();
        }, 2000)
    }

    render(randomSeed, init){

        deleteAllChildren(this.#CanvasSelector)

        this.map.grid.forEach( (row, rowIndex) => {
            const RowElement = `<div class='row'></div>`;
            createElement(this.#CanvasSelector, RowElement);
            
            row.forEach( (cell, cellIndex) => {
                // Randomize Value on init, and sets position of each cell
                if (randomSeed && init) cell.value = randomMinMax(0, 1); cell.position = [rowIndex, cellIndex];
            
                const CellElement = `
                <div class='cell cell${cell.value}'>
                ${cell.value}
                </div>`;
                createElement(this.#LastRowSelector, CellElement);
            })
        })
    }

    changeMapCellValues(){
        this.map.grid.forEach( row => {
            row.forEach( cell => {
                cell.value = this.gameOfLifeLogic(cell);
            })
        })
    }

    gameOfLifeLogic(cell){
        // Saves cross directions to a cell object
        cell.crossDirections = this.getCrossDirections(cell.position);

        // Array containing cross cells values [0, 1, 0, undefined]
        let values = [
            this.getCellValue(cell.crossDirections.top, cell.position[1]),
            this.getCellValue(cell.crossDirections.bottom, cell.position[1]),
            this.getCellValue(cell.position[0], cell.crossDirections.left),
            this.getCellValue(cell.position[0], cell.crossDirections.right),
        ]


        let aliveCellsAround = values.filter(x => x==1).length;
            
        switch (cell.value){
            case 0:
                if (aliveCellsAround == 3) return 1
            case 1:
                if (aliveCellsAround == 1 || aliveCellsAround == 4) return 0
            default: return cell.value
        }
    }

    renderSteps(){
        this.changeMapCellValues();
        this.render(false, false);
    }

    getCrossDirections(cellsPosition){
        // This function gets cell neighbourgs in cross pattern
        // Validator function prevents position to go behind the grid border (-1 etc)
        // Undefine if position is off the grid
        function validator(crossDirectionsObject, map){
            if(crossDirectionsObject.top < 0) crossDirectionsObject.top = undefined;
            if(crossDirectionsObject.bottom >= map.length) crossDirectionsObject.bottom = undefined;
            if(crossDirectionsObject.left < 0) crossDirectionsObject.left = undefined;
            if(crossDirectionsObject.right >= map[0].length) crossDirectionsObject.right = undefined;

            return crossDirectionsObject
        }

        let crossDirections = {
            top: cellsPosition[0] - 1,
            bottom: cellsPosition[0] + 1,
            left: cellsPosition[1] - 1,
            right: cellsPosition[1] + 1,
        }
        return validator(crossDirections, this.map.grid) 
    
    }

    getCellValue(x, y){
        if(x != undefined && y != undefined) {
            return this.map.grid[x][y].value
        }
    }
}


function createElement(parentSelector, elementType){
    return document.querySelector(parentSelector).insertAdjacentHTML('beforeend', elementType);
}

function deleteAllChildren(parentSelector){
    return document.querySelector(parentSelector).replaceChildren();
}


function randomMinMax(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
  }
  