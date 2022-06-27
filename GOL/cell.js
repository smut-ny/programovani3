const DEFAULT_OPTIONS = {
    size: 20,
    value: 0,
    position: []
}

export default class Cell {
    constructor(options) {
        Object.entries({ ...DEFAULT_OPTIONS, ...options }).forEach(([key, value]) => {
            this[key] = value
        })
    }
}