import numpy as np

# Read the file
with open("../data/20231206_input.txt", "r") as f:
    # with open("test.txt", "r") as f:
    data = f.read()

# Get rid of the newline at the end
data = data.strip()

# Split the data into a list
data = data.split("\n")

times = data[0].split(":")[1].split(" ")
# Join all the times together ignoring the spaces
times = int("".join(times))
max_distance = data[1].split(":")[1].split(" ")
# Join all the distances together ignoring the spaces
max_distance = int("".join(max_distance))

# Equation
# -x^2 + times * x - max_distance > 0
# Solver for x
x_plus = (times + np.sqrt(times**2 - 4 * max_distance)) / 2
x_minus = (times - np.sqrt(times**2 - 4 * max_distance)) / 2


# Find the value of equation at x_plus and x_minus
def get_equation_value(x):
    return -(x**2) + times * x - max_distance


print(get_equation_value(x_plus))
print(get_equation_value(x_minus))

# Find the difference between the two values
print(int(x_plus - x_minus) + 1)
