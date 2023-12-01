import numpy as np
import matplotlib.pyplot as plt

# Activate the latex text rendering
plt.rc("text", usetex=True)
plt.rc("font", family="serif")

# Read the test_input.txt file contents in a list
with open("test_input.txt") as f:
    content = f.readlines()

content = content[0]

# Count the numbers of ( and ) in the content
n_open = content[0:].count("(")
n_close = content[0:].count(")")

# Get the difference between the two
diff = n_open - n_close

# Print the result
print(f"Number of ( : {n_open}")
print(f"Number of ) : {n_close}")
print(f"Floor number : {diff}")

floor = []
for i in range(len(content)):
    if content[i] == "(":
        floor.append(1)
    elif content[i] == ")":
        floor.append(-1)
    else:
        floor.append(0)

# Find the first index where the floor number is -1
index_min = np.where(np.cumsum(floor) == -1)[0][0]
print(index_min + 1)

# Plot the cumulative sum of the floor number as a function of the index
plt.plot(np.cumsum(floor))
plt.xlabel("Index")
plt.ylabel("Floor number")
plt.title("Floor number as a function of the index")
plt.grid()
plt.tight_layout()
plt.savefig("floor_number.png", dpi=300)
