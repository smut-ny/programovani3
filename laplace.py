# Global functions
import random

# 1. generate map
def generateMap(x, y, tiles_number):

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
        def getRandomCoords(x, y, random_coords_number):
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

        random_coords_list = getRandomCoords(x, y, tiles_number)
        blank_map = map
        final_map = setValues(random_coords_list, blank_map, values)

        return final_map



    tiles_values = tilesRandomValueGenerator(10, tiles_number)
    blank_map = createBlankMap(x, y, ".")
    map = setValuesToMap(tiles_values, blank_map, x, y, 5)

    return map

print(
generateMap(5, 5, 5)
)