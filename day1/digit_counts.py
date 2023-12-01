import numpy as np
import re

# Read the input.txt file contents in a list
with open("input.txt") as f:
    content = f.readlines()

# Get rid of the \n at the end of each line
content = [x.strip() for x in content]

# Get the list of numbers in each line
first_numbers = []
last_numbers = []
for i in range(len(content[0:])):
    numbers = re.findall(r"\d+", content[i])
    first_numbers.append(int(numbers[0][0]))
    last_numbers.append(int(numbers[-1][-1]))

# Print the result
# for i, j, k in zip(range(10), first_numbers, last_numbers):
#     print(f"Line {i+1} : {j} {k}")


# Make the numbers
first_numbers = np.array(first_numbers)
last_numbers = np.array(last_numbers)
first_numbers = first_numbers * 10
last_numbers = last_numbers * 1
numbers = first_numbers + last_numbers
sum_numbers = np.sum(numbers)
print(sum_numbers)
