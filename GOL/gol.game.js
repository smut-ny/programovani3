const DEFAULT_OPTIONS = {
    runs: true,
    map: { grid: [[]] }
}

export default class Game {
    constructor(options) {
        Object.entries({ ...DEFAULT_OPTIONS, ...options }).forEach(([key, value]) => {
            this[key] = value
        })
    }

    render(){
        this.map.grid.forEach( e => {
            let row = document.createElement('div')
            row.classList = "row"
            row.innerText = e
            document.querySelector('body').append(row)
        })
    }
}