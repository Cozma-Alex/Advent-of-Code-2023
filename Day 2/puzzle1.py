with (open('input-puzzle.txt', 'r') as file):
    contents = file.readlines()
    sums = 0
    game_number = 1
    for line in contents:
        ok = 1
        sets = line.split(': ')[1]
        game_number = int(line.split(': ')[0].split(' ')[1])
        sets.strip()
        sets_split = sets.split('; ')
        for set_ in sets_split:
            types_appearances = {'red': 0, 'green': 0, 'blue': 0}
            cube_type = set_.split(', ')
            for type_ in cube_type:
                type_ = type_.strip()
                if type_.split(' ')[1] in types_appearances:
                    types_appearances[type_.split(' ')[1]] += int(type_.split(' ')[0])
            if types_appearances['red'] > 12 or types_appearances['green'] > 13 or types_appearances['blue'] > 14:
                ok = 0
                break
        if ok == 1:
            sums += game_number

print(sums)
