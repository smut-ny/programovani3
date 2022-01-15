# Global functions
from decimal import DivisionByZero
import random
import numpy
import math
import json


def prettyPrintVector(vector_data):
    for line in vector_data:
        print(*line)

def mean(list):
    output = 0
    for i in list:
        output += i
    
    if output > 0:
        return math.floor(output / len(list))
    else:
        return "."

def getEmptyValuesCoords(map):
    coords = []

    for row_index, row in enumerate(map):
        for index, value in enumerate(row):
            if value == blank_character:
                coords.append([row_index, index])

    return coords

def my_flatten(lists):
    flatten_list = []

    for i in lists:
        if type(i) is not list:
            flatten_list.append(i)
        else:
            flatten_list.extend(my_flatten(i))

    return flatten_list

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

    def getValues(empty_value_coords, map_inpt):
        def getCrossValues(coord, map):
            output = []

            top = numpy.add(coord, [-1, 0])
            right = numpy.add(coord, [0, +1])
            bot = numpy.add(coord, [+1, 0])
            left =  numpy.add(coord, [0, -1])
            
            # Skip minus indexes
            if coord[0] == 0:
                top = [2000, 2000]
            if coord[1] == 0:
                left = [2000, 2000]

            coords = [top, right, bot, left]
            
            # get values
            for count, value in enumerate(coords):
                coordY = value[0]
                coordX = value[1]

                try:
                    output.append(map[coordY][coordX])
                except IndexError:
                    output.append("null")

            return output

        def getAllCrossValues(empty_value_coords, map):
            allCrossValues = {}

            for value in empty_value_coords:
                allCrossValues[str(value)] = getCrossValues(value, map)
            
            return allCrossValues

        return getAllCrossValues(empty_value_coords, map_input)
        
    def step(values, map):
        output_map = map

        for key, value in values.items():
            keyList = json.loads(key)
            coordY = keyList[0]
            coordX = keyList[1]
            only_intgrs = [x for x in value if not isinstance(x, str)]
            mean_output = mean(only_intgrs)

            output_map[coordY][coordX] = mean_output
        
        return output_map

    # main recursive function for each step
    def walk(map):
        empty_values_coords = getEmptyValuesCoords(map)
        values = getValues(empty_values_coords, map)

        if '.' in my_flatten(map):
                print(map, prettyPrintVector(map), "\n")
                return walk(step(values, map))
        else:
            return map, prettyPrintVector(map)


        

    all_crossValues = getValues(empty_value_coords, map_input)
    
    return walk(step(all_crossValues, map_input))



# 3. Init
laplace_map = generateMap(5, 5, 5, blank_character)
print(laplaceSteps(laplace_map))