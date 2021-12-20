# Global functions
import random

def prettyPrintVector(vector_data):
    for line in vector_data:
        print(*line)

# Global vars
blank_character = "."

# 1. generate map
def generateMap(x, y, tiles_number, blank_character):

    def tilesRandomValueGenerator(random_number_cap, count):
        tiles_list = []
        i = 0

        while i < count:
            tiles_list.append(random.randint(1, random_number_cap))
            i += 1

        return tiles_list

    def createBlankMap(x, y, blank_character):
        map = []
        row = []

        for i in range(x):
            row.append(blank_character)

        for i in range(y):
            map.append(row.copy())
            # Use .copy otherwise it wont work

        return map
        
    def setValuesToMap(values, map, x, y, tiles_number):
        def createRandomCoords(x, y, random_coords_number):
            coords_list = []

            while len(coords_list) < random_coords_number:

                x_coord = random.randint(0, (y - 1))
                y_coord = random.randint(0, (x - 1))
                coord = [x_coord, y_coord]

                # Skip duplicates
                if coord not in coords_list:
                    coords_list.append(coord)
                else:
                    continue

            return coords_list
            
        def setValues(coords, map, values_to_add):

            for i in range(len(coords)):
                coord_x = coords[i][0]
                coord_y = coords[i][1]
                value = values_to_add[i]

                map[coord_y][coord_x] = value
            
            return map

        def getEmptyValuesCoords(map):
            coords = []
            
            for row in map:
                for index, value in enumerate(row):
                    if value == blank_character:
                        coords.append([map.index(row), index])

            return coords

        random_coords_list = createRandomCoords(x, y, tiles_number)
        blank_map = map
        final_map = setValues(random_coords_list, blank_map, values)

        output = {
            "map": final_map,
            "data": {
                "tile_values": values,
                "tile_coords": random_coords_list,
                "empty_value_coords": getEmptyValuesCoords(map),
                "info": "Coords are zero indexed"
            }
        }

        return output



    tiles_values = tilesRandomValueGenerator(10, tiles_number)
    blank_map = createBlankMap(x, y, blank_character)
    map_output = setValuesToMap(tiles_values, blank_map, x, y, 5)

    return map_output


# 2. laplace function

def laplaceSteps(map):
    map_input = map["map"]
    empty_value_coords = map["data"]["empty_value_coords"]

    def step():
        pass

    return prettyPrintVector(map_input), empty_value_coords




# 3. Init
laplace_map = generateMap(5, 5, 5, blank_character)

print(laplaceSteps(laplace_map))