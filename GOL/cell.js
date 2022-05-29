const DEFAULT_OPTIONS = {
    size: 20,
    filler: 0
}

export default class Cell {
    constructor(options) {
        Object.entries({ ...DEFAULT_OPTIONS, ...options }).forEach(([key, value]) => {
            this[key] = value
        })
    }
}