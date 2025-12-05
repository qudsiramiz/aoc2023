import numpy as np

file_path = "data/input_v02.txt"
with open(file_path, "r") as f:
    for line in f:
        line = line.strip()

all_ranges = line.split(",")

start_list = np.zeros(len(all_ranges))
stop_list = np.zeros(len(all_ranges))
for i, xx in enumerate(all_ranges):
    start_list[i] = xx.split("-")[0]
    stop_list[i] = xx.split("-")[1]

invalid_ids = []

for start, stop in zip(start_list[:], stop_list[:]):
    range_id = np.linspace(start, stop, int(stop - start) + 1, endpoint=True)
    range_id_str_list = [str(int(xx)) for xx in range_id]
    for xx in range_id_str_list:
        len_xx = len(xx)
        # Part 1
        # k = int(len_xx / 2)
        # if xx[:k] == xx[k:]:
        #     invalid_ids.append(xx)

        # Part 2
        for k in range(1, len_xx // 2 + 1):
            if len_xx % k == 0:
                if xx == xx[:k] * (len_xx // k):
                    invalid_ids.append(xx)
                    break

int_invalid_ids = np.array([int(xx) for xx in invalid_ids])
print(sum(int_invalid_ids))
