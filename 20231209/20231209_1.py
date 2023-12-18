import numpy as np


# Define a function to find the difference between the consecutive elements of an array until all the
# elements are zero
def find_diff(arr):
    # Initialize the counter
    counter = 0
    last_elemt = []
    arr_last_val = arr[-1]

    # While the array contains non-zero elements
    while np.any(arr != 0):
        # Find the difference between the consecutive elements
        arr = np.diff(arr)
        last_elemt.append(arr[-1])
        # print(arr)
        # print(last_elemt)

        # Increment the counter
        counter += 1

    # Sum the last elements
    last_elemt_sum = sum(last_elemt) + arr_last_val
    # Return the counter
    return counter, last_elemt, last_elemt_sum


# Read the file
with open("../data/20231209_input.txt", "r") as f:
    # with open("test.txt", "r") as f:
    data = f.read()

# Split the data into a list
data = data.split("\n")

# Remove the last empty element
data.pop()

# Split each line into a list of integers separated by a space
data = [line.split(" ") for line in data]

# Convert the strings to integers
data = [[int(i) for i in line] for line in data]

# Convert the list of lists to a numpy array
data = np.array(data)
last_elemt_list = []
last_elemt_sum_list = []

for i in range(data.shape[0]):
    # Find the difference between the consecutive elements of the array
    counter, last_elemt, last_elemt_sum = find_diff(data[i])
    last_elemt_list.append(last_elemt)
    last_elemt_sum_list.append(last_elemt_sum)

# Print the sum of last_elemt_sum_list
print(f"The sum of all extrapolated items is {sum(last_elemt_sum_list)}")
