const DEFAULT_OPTIONS = {

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
        this.render();
    }

    render(){
        this.map.grid.forEach( row => {
            const RowElement = `<div class='row'></div>`
            createElement(this.#CanvasSelector, RowElement);

            row.forEach( cell => {
                const CellElement = `<div class='cell'>${cell}</div>`;
                createElement(this.#LastRowSelector, CellElement);
            })
        })
    }
}


function createElement(parentSelector, elementType){
    return document.querySelector(parentSelector).insertAdjacentHTML('beforeend', elementType);
}