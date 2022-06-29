const DEFAULT_OPTIONS = {
    dimension: [10, 10]
}

export default class Map {

    constructor(options) {
        Object.entries({ ...DEFAULT_OPTIONS, ...options }).forEach(([key, value]) => {
            this[key] = value
        })

        this.grid = createGrid(this.dimension, this.cell)
    }
}

// TODO DEEP COOPY
function createGrid(array, cell){
    let row = [];
    let grid = [];

    for (let i = 0; i < array[0]; i++){
        row.push(new cell);
    }
    
    for (let i = 0; i < array[1]; i++){
        grid.push(structuredClone(row));
    }
    
    return grid
}