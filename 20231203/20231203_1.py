# Read the input file
with open("input.txt") as f:
    content = f.readlines()

# Remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

# Get the symbol list
symbols = []
for line in content:
    for char in line:
        if char not in symbols and not char.isdigit() and char != ".":
            symbols.append(char)

# Find the indices of all the numbers in each line and store them in a list
number_indices = []
for line in content:
    number_indices.append([])
    ind_val = 0
    for char in line:
        # If the character is a digit, add it to the list
        if char.isdigit():
            number_indices[-1].append(ind_val)
        ind_val += 1


def valid_pos(i, j):
    """
    Check if the position (i, j) is valid. A position is valid if within 2 x 2 square of it, there is
    a symbol.
    """
    # Check if the position is valid
    if i > 0 and j > 0:
        if content[i - 1][j - 1] in symbols:
            return True
    if i > 0:
        if content[i - 1][j] in symbols:
            return True
    if i > 0 and j < len(content[i]) - 1:
        if content[i - 1][j + 1] in symbols:
            return True
    if j > 0:
        if content[i][j - 1] in symbols:
            return True
    if j < len(content[i]) - 1:
        if content[i][j + 1] in symbols:
            return True
    if i < len(content) - 1 and j > 0:
        if content[i + 1][j - 1] in symbols:
            return True
    if i < len(content) - 1:
        if content[i + 1][j] in symbols:
            return True
    if i < len(content) - 1 and j < len(content[i]) - 1:
        if content[i + 1][j + 1] in symbols:
            return True
    return False


def compute_number(line_number, grouped_indices):
    if len(grouped_indices) == 1:
        return int(content[line_number][grouped_indices[0]])
    elif len(grouped_indices) == 2:
        return int(content[line_number][grouped_indices[0]]) * 10 + int(
            content[line_number][grouped_indices[1]]
        )
    elif len(grouped_indices) == 3:
        return (
            int(content[line_number][grouped_indices[0]]) * 100
            + int(content[line_number][grouped_indices[1]]) * 10
            + int(content[line_number][grouped_indices[2]])
        )
    elif len(grouped_indices) == 4:
        print("Error: Number has 4 digits")
        return None


# In number_indices, check if the position is valid, if it is then add it to the list
valid_number_indices = []
for i in range(len(number_indices)):
    valid_number_indices.append([])
    for j in range(len(number_indices[i])):
        if valid_pos(i, number_indices[i][j]):
            valid_number_indices[-1].append(number_indices[i][j])

# For valid indices, check if in the same row, within j -2 to j + 2, there is a number, if there is
# then add it to the list of number values
additional_valid_number_indices = []
row_num = [10]
for i in range(len(valid_number_indices)):
    # for i in range(0, 19):
    additional_valid_number_indices.append(valid_number_indices[i])
    for j in valid_number_indices[i]:
        for k in range(-2, 3):
            if j + k >= 0 and j + k < len(content[i]):
                # Check if j + k is a digit
                if content[i][j + k].isdigit():
                    if k > 0:
                        # If j + k - 1 ais not a digit then continue
                        if not content[i][j + k - 1].isdigit():
                            continue
                    elif k < 0:
                        # If j + k + 1 is not a digit then continue
                        if not content[i][j + k + 1].isdigit():
                            continue
                    # print(j + k)
                    # Check if j + k is already in the list
                    if j + k not in additional_valid_number_indices[-1]:
                        additional_valid_number_indices[-1].append(j + k)
    additional_valid_number_indices[-1].sort()

grouped_list = []
for sublist in additional_valid_number_indices:
    group = []
    for i, num in enumerate(sublist):
        if i == 0 or num != sublist[i - 1] + 1:
            group.append([num])
        else:
            group[-1].append(num)
    grouped_list.append(group)

number_list = []
for i in range(len(grouped_list)):
    number_list.append([])
    for j in range(len(grouped_list[i])):
        number_list[-1].append(compute_number(i, grouped_list[i][j]))

# Sum all the values in the number list
print(sum([sum(x) for x in number_list]))
