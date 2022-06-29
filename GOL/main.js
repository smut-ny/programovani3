import map from "./map.js"
import cell from "./cell.js"
import game from "./game.js"


const Map = new map({cell: cell, dimension: [50, 50] })
const Game = new game({ map: Map, speed:5000 })


Game.start()