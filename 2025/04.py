import numpy as np

file_path = "data/input_v04.txt"
line_list = []
with open(file_path, "r") as f:
    for line in f:
        line_list.append(line.strip())

roll_location = np.zeros((len(line_list), len(line_list[0])), dtype=bool)

for i in range(roll_location.shape[0]):
    for j in range(roll_location.shape[1]):
        if line_list[i][j] == "@":
            # print(line_list[i][j])
            roll_location[i][j] = True
            # print(roll_location[i][j])


def compute_roll_matrix(roll_matrix, roll_location):
    for i in range(roll_matrix.shape[0]):
        for j in range(roll_matrix.shape[1]):
            neighbours = np.zeros(8, dtype=bool)
            if i >= 1 and j >= 1:
                neighbours[0] = roll_location[i - 1][j - 1]
            if i >= 1:
                neighbours[1] = roll_location[i - 1][j]
            if i >= 1 and j < 138:
                neighbours[2] = roll_location[i - 1][j + 1]
            if j >= 1:
                neighbours[3] = roll_location[i][j - 1]
            if j < 138:
                neighbours[4] = roll_location[i][j + 1]
            if i < 138 and j > 0:
                neighbours[5] = roll_location[i + 1][j - 1]
            if i < 138:
                neighbours[6] = roll_location[i + 1][j]
            if i < 138 and j < 138:
                neighbours[7] = roll_location[i + 1][j + 1]

            if sum(neighbours) >= 4:
                roll_matrix[i][j] = False
    return roll_matrix, sum(sum(roll_matrix))


roll_matrix = roll_location.copy()
number_of_rolls = sum(sum(roll_location))
previous_count = 0
new_count = 1
all_counts = []

while new_count > 0:
    roll_matrix, new_count = compute_roll_matrix(roll_matrix, roll_location)
    roll_location[roll_matrix] = False
    roll_matrix = roll_location.copy()
    # previous_count = new_count
    print(sum(sum(roll_matrix)), previous_count, new_count)
    all_counts.append(new_count)


print(sum(all_counts))