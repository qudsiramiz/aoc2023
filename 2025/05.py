import numpy as np

file_path = "data/input_v05.txt"
line_list = []
with open(file_path, "r") as f:
    for line in f:
        line_list.append(line.strip())

line_list = np.array(line_list)

max_fresh_ind = np.where(line_list == "")[0][0]

list_of_fresh = line_list[:max_fresh_ind]
list_of_all_ing = line_list[max_fresh_ind + 1:]

counts_fresh = 0

fresh_ranges = [tuple(map(int, xx.split("-"))) for xx in list_of_fresh]
fresh_ing = [xx for xx in list_of_all_ing if any(a <= int(xx) <= b for a, b in fresh_ranges)]
print(len(fresh_ing))

intervals = sorted(fresh_ranges)
merged = []
for a, b in intervals:
    if not merged or a > merged[-1][1] + 1:
        merged.append([a, b])
    else:
        merged[-1][1] = max(merged[-1][1], b)
all_counts = sum(b - a + 1 for a, b in merged)

print(all_counts)
