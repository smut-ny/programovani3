import GameLogic from "./gameLogic.js"


const DEFAULT_OPTIONS = {
    runs: true,
    speed: 1000,
    map: { grid: [[]] }
}

export default class Game {

    constructor(options) {
        Object.entries({ ...DEFAULT_OPTIONS, ...options }).forEach(([key, value]) => {
            this[key] = value;
        })
    }

    start(){
        const gameLogic = new GameLogic({ runs: this.runs, map: this.map, speed: this.speed })
        gameLogic.startGame()
    }
}