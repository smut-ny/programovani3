const DEFAULT_OPTIONS = {
    dimension: [10, 10]
}

export default class Map {

    constructor(options) {
        Object.entries({ ...DEFAULT_OPTIONS, ...options }).forEach(([key, value]) => {
            this[key] = value
        })

        this.grid = createGrid(this.dimension, this.cell.filler)
    }
}

function createGrid(array, filler){
    let row = new Array(array[0]).fill(filler)
    let grid = new Array(array[1]).fill(row)
    
    return grid
}