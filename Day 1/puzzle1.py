with (open('input-puzzle1.txt', 'r') as file):
    contents = file.readlines()
    sums = 0
    for line in contents:
        i = 0
        while not line[i].isdigit():
            i += 1
        first_digit = int(line[i])
        i = len(line) - 1
        while not line[i].isdigit():
            i -= 1
        last_digit = int(line[i])
        number = first_digit * 10 + last_digit
        sums += number

print(sums)
