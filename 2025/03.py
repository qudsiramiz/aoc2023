import numpy as np

file_path = "data/input_v03.txt"
line_list = []
with open(file_path, "r") as f:
    for line in f:
        line_list.append(line.strip())

max_number_list = np.zeros(len(line_list))


def find_max(line_val, max_number):
    for i in range(len(line_val) - 1):
        tens_digit = int(line_val[i])
        remaining_line = line_val[i + 1:]
        for ones_digit in remaining_line:
            if tens_digit * 10 + int(ones_digit) > max_number:
                max_number = tens_digit * 10 + int(ones_digit)
            else:
                continue

    return max_number


for i, line in enumerate(line_list[:]):
    max_number = find_max(line, max_number_list[i])
    max_number_list[i] = max_number
    print(i, max_number, sum(max_number_list))

print(sum(max_number_list))
