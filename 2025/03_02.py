import numpy as np

file_path = "data/input_v03.txt"
line_list = []
with open(file_path, "r") as f:
    for line in f:
        line_list.append(line.strip())

max_number_list = np.zeros(len(line_list))


def find_max(line_val, max_number_of_digits):
    digits = [int(ch) for ch in line_val if ch.isdigit()]
    n = len(digits)

    final_digit = []
    start = 0
    for xx in range(max_number_of_digits):
        end = n - (max_number_of_digits - xx) + 1
        max_d = -1
        max_idx = start
        for idx in range(start, end):
            d = digits[idx]
            if d > max_d:
                max_d = d
                max_idx = idx
        final_digit.append(str(max_d))
        start = max_idx + 1
    return int("".join(final_digit))


max_number_of_digits = 12
for i, line in enumerate(line_list[:]):
    max_number = find_max(line, max_number_of_digits)
    max_number_list[i] = max_number
    print(i, max_number, sum(max_number_list))

print(sum(max_number_list))
