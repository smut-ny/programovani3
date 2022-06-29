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
            
                const CellElement = `<div class='cell cell${cell.value}'>${cell.value}</div>`;
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
        cell.crossValues = this.getCrossDirections(cell.position);
        let values = [
            this.getCellValue(cell.position[0], cell.crossValues.top),
            this.getCellValue(cell.position[0], cell.crossValues.bottom),
            this.getCellValue(cell.position[1], cell.crossValues.left),
            this.getCellValue(cell.position[1], cell.crossValues.right),
        ]

        let aliveCellsAround = values.filter(x => x==1).length == 3;
            
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

    getCrossDirections(position){
        // Undefine if position is off the grid
        function crossDirectionsValidator(crossValuesObject, map){
            if(crossValuesObject.top < 0) crossValuesObject.top = undefined;
            if(crossValuesObject.bottom >= map.length) crossValuesObject.bottom = undefined;
            if(crossValuesObject.left < 0) crossValuesObject.left = undefined;
            if(crossValuesObject.right >= map[0].length) crossValuesObject.right = undefined;

            return crossValuesObject
        }

        let crossValues = {
            top: position[0] - 1,
            bottom: position[0] + 1,
            left: position[1] - 1,
            right: position[1] + 1,
        }
        return crossDirectionsValidator(crossValues, this.map.grid) 
    
    }

    getCellValue(x, y){
        if(x && y ) 
        return this.map.grid[x][y].value
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
  