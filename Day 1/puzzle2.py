with (open('input-puzzle1.txt', 'r') as file):
    possible_numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                        'nine': 9}
    contents = file.readlines()
    sums = 0
    for line in contents:
        first_digit = 0
        last_digit = 0
        line.strip()
        for i in range(len(line)):
            if line[i].isdigit():
                last_digit = int(line[i])
                if first_digit == 0:
                    first_digit = int(line[i])
            else:
                if len(line) - i > 5:
                    test_str = line[i:i + 5]
                    if test_str in possible_numbers:
                        last_digit = possible_numbers[test_str]
                        if first_digit == 0:
                            first_digit = possible_numbers[test_str]
                if len(line) - i > 4:
                    test_str = line[i:i + 4]
                    if test_str in possible_numbers:
                        last_digit = possible_numbers[test_str]
                        if first_digit == 0:
                            first_digit = possible_numbers[test_str]
                if len(line) - i > 3:
                    test_str = line[i:i + 3]
                    if test_str in possible_numbers:
                        last_digit = possible_numbers[test_str]
                        if first_digit == 0:
                            first_digit = possible_numbers[test_str]
        number = first_digit * 10 + last_digit
        sums += number

print(sums)
