def recreate_number(params, engine_):
    line_ = engine_[params[0]]
    number_str = ""
    number_str_other_side = ""
    prms = params[1] + 1
    while line_[prms].isdigit():
        number_str_other_side += line_[prms]
        prms += 1
    while line_[params[1]].isdigit():
        number_str += line_[params[1]]
        params[1] -= 1
    number_str_other_side = number_str_other_side[::-1]
    number_str_other_side += number_str
    return int(number_str_other_side[::-1])


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
        numbers = {}
        count = 0
        for j in range(len(engine[i])):
            if engine[i][j] == '*':
                count = 0
                if engine[i - 1][j - 1].isdigit() or engine[i - 1][j].isdigit() or engine[i - 1][j + 1].isdigit():
                    if (not engine[i - 1][j].isdigit()) and engine[i - 1][j + 1].isdigit() and engine[i - 1][
                        j - 1].isdigit():
                        count += 2
                        numbers[count - 1] = [i - 1, j - 1]
                        numbers[count] = [i - 1, j + 1]
                    else:
                        count += 1
                        if engine[i - 1][j - 1].isdigit():
                            numbers[count] = [i - 1, j - 1]
                        if engine[i - 1][j + 1].isdigit():
                            numbers[count] = [i - 1, j + 1]
                        if engine[i - 1][j].isdigit():
                            numbers[count] = [i - 1, j]
                if engine[i][j + 1].isdigit():
                    count += 1
                    numbers[count] = [i, j + 1]
                if engine[i][j - 1].isdigit():
                    count += 1
                    numbers[count] = [i, j - 1]
                if engine[i + 1][j - 1].isdigit() or engine[i + 1][j].isdigit() or engine[i + 1][j + 1].isdigit():
                    if (not engine[i + 1][j].isdigit()) and engine[i + 1][j + 1].isdigit() and engine[i + 1][
                        j - 1].isdigit():
                        count += 2
                        numbers[count - 1] = [i + 1, j - 1]
                        numbers[count] = [i + 1, j + 1]
                    else:
                        count += 1
                        if engine[i + 1][j - 1].isdigit():
                            numbers[count] = [i + 1, j - 1]
                        if engine[i + 1][j + 1].isdigit():
                            numbers[count] = [i + 1, j + 1]
                        if engine[i + 1][j].isdigit():
                            numbers[count] = [i + 1, j]
            if count == 2:
                sums += (recreate_number(numbers[1], engine) * recreate_number(numbers[2], engine))
                count = 0

print(sums)
