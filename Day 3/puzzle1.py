with (open('input-puzzle.txt', 'r') as file):
    contents = file.readlines()
    sums = 0
    engine = []
    lens = 0
    for line in contents:
        line = line.strip()
        lens = len(line)
        engine_line = list(char for char in line)
        engine_line.insert(0, '.')
        engine_line.append('.')
        engine.append(engine_line)

    point_list = ['.'] * (lens + 1)
    engine.insert(0, point_list)
    engine.append(point_list)

    for i in range(len(engine)):
        number = 0
        verif = False
        for j in range(len(engine[i])):
            if engine[i][j].isdigit():
                number = number * 10 + int(engine[i][j])
                for k in range(i - 1, i + 2):
                    for q in range(j - 1, j + 2):
                        if engine[k][q] in '`~!@#$%^&*|\()_+-={[}]:;<,>/?':
                            verif = True
            else:
                if verif:
                    sums += number
                number = 0
                verif = False

print(sums)
