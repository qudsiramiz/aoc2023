import numpy as np


# Define a function to find the difference between the consecutive elements of an array until all the
# elements are zero in reverse order
def find_diff(arr):
    # Initialize the counter
    counter = 0
    first_elemt = []
    arr_first_val = arr[0]
    first_elemt.append(arr_first_val)

    # While the array contains non-zero elements
    while np.any(arr != 0):
        # Find the difference between the consecutive elements starting from the last element
        arr = np.diff(arr[::1])
        first_elemt.append(arr[0])
        # print(arr)
        # print(first_elemt)

        # Increment the counter
        counter += 1

    # Sum the first elements
    first_elemt_sum = sum(first_elemt[::2]) - sum(first_elemt[1::2])
    # Return the counter
    return counter, first_elemt, first_elemt_sum


# Read the file
with open("../data/20231209_input.txt", "r") as f:
    # with open("test.txt", "r") as f:
    data = f.read()

# Split the data into a list
data = data.split("\n")

# Remove the empty elements
data.pop()

# Split each line into a list of integers separated by a space
data = [line.split(" ") for line in data]

# Convert the strings to integers
data = [[int(i) for i in line] for line in data]

# Convert the list of lists to a numpy array
data = np.array(data)
first_elemt_list = []
first_elemt_sum_list = []

for i in range(data.shape[0]):
    # Find the difference between the consecutive elements of the array
    counter, first_elemt, first_elemt_sum = find_diff(data[i])
    first_elemt_list.append(first_elemt)
    first_elemt_sum_list.append(first_elemt_sum)

# Print the sum of first_elemt_sum_list
print(f"The sum of all extrapolated items is {sum(first_elemt_sum_list)}")
