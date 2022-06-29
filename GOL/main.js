import map from "./map.js"
import cell from "./cell.js"
import game from "./game.js"


window.gameMap = new map({cell: cell, dimension: [50, 5] })
window.Game = new game({ map: gameMap, speed: 100 })


Game.start()    