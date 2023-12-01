import numpy as np
import re
import matplotlib.pyplot as plt

# Read the input.txt file contents in a list
with open("input.txt") as f:
    content = f.readlines()

# Get rid of the \n at the end of each line
content = [x.strip() for x in content]

# Define a ddictionary with number written in words as keys and their corresponding digits as values
numbers_dict = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

num_list = []
for content_val in content:
    numbers = re.findall(
        r"(?=(\d|zero|one|two|three|four|five|six|seven|eight|nine))", content_val
    )
    if len(numbers[0]) > 1:
        number_ten = numbers_dict[numbers[0]]
    else:
        number_ten = numbers[0]
    if len(numbers[-1]) > 1:
        number_one = numbers_dict[numbers[-1]]
    else:
        number_one = numbers[-1]
    number = int(number_ten) * 10 + int(number_one)
    num_list.append(number)

# Save num_list to a file
with open("input_new.txt", "w+") as num_file:
    for num in num_list:
        num_file.write(f"{num}\n")

# Sum the numbers in the list
sum_numbers = np.sum(num_list)
print(sum_numbers)
