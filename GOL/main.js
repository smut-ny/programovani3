import map from "./map.js"
import cell from "./cell.js"
import game from "./game.js"

const Cell = new cell()
const Map = new map({cell: Cell})
const Game = new game({ map: Map })


Game.start()