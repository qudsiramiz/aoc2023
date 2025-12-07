import numpy as np

file_path = "data/input_v06.txt"
line_list = []
with open(file_path, "r") as f:
    for line in f:
        line_list.append(line.strip())

line_list = np.array(line_list)
number_list = line_list[:-1]
math_operations = line_list[-1]
math_operations_list = [xx for xx in math_operations if xx.strip() != ""]

list_of_numbers = np.zeros((len(line_list) - 1, len(math_operations_list)))

for i in range(list_of_numbers.shape[0]):
    new_number_list = number_list[i].split(" ")
    list_of_numbers[i] = np.array([xx for xx in new_number_list if xx.strip() != ""])

column_values = np.zeros(list_of_numbers.shape[1])


def compute_values(input_array, operation):
    if operation == "*":
        return np.prod(input_array)
    elif operation == "+":
        return np.sum(input_array)


for i in range(list_of_numbers.shape[1]):

    column_values[i] = compute_values(list_of_numbers[:, i], math_operations_list[i])

print(sum(column_values))
