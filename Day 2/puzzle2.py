with (open('input-puzzle.txt', 'r') as file):
    contents = file.readlines()
    sums = 0
    for line in contents:
        sets = line.split(': ')[1]
        sets.strip()
        sets_split = sets.split('; ')
        types_appearances = {'red': 0, 'green': 0, 'blue': 0}
        for set_ in sets_split:
            red = 0
            green = 0
            blue = 0
            cube_type = set_.split(', ')
            for type_ in cube_type:
                type_ = type_.strip()
                if type_.split(' ')[1] == 'red':
                    red += int(type_.split(' ')[0])
                if type_.split(' ')[1] == 'green':
                    green += int(type_.split(' ')[0])
                if type_.split(' ')[1] == 'blue':
                    blue += int(type_.split(' ')[0])
            if types_appearances['blue'] < blue:
                types_appearances['blue'] = blue
            if types_appearances['green'] < green:
                types_appearances['green'] = green
            if types_appearances['red'] < red:
                types_appearances['red'] = red
        power = types_appearances['red'] * types_appearances['green'] * types_appearances['blue']
        sums += power

print(sums)
