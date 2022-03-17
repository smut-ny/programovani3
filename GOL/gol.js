import map from "./gol.map.js"
import cell from "./gol.cell.js"
import game from "./gol.game.js"

const Cell = new cell()
const Map = new map({cell: Cell})
const Game = new game({ map: Map })

console.log(Map);

Game.render()