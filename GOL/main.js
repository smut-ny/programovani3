import map from "./map.js"
import cell from "./cell.js"
import game from "./game.js"


const Map = new map({cell: cell, dimension: [20, 40] })
const Game = new game({ map: Map })


Game.start()