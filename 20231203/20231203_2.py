# Read the input file
with open("../data/20231203_input.txt") as f:
    content = f.readlines()

# Remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

symbols = ["*"]

# Find the indices of all places where there is a symbol
symbol_indices = []
for i in range(len(content)):
    symbol_indices.append([])
    for j in range(len(content[i])):
        if content[i][j] == symbols[0]:
            symbol_indices[-1].append(j)


def valid_symbol(i, j):
    """
    A position is valid if within 2 x 2 square of it, there is are exactly 2 digits
    """
    digit_count = 0
    # In row = i - 1, check if there is a digit in either of the columns = j - 1, j, j + 1, and j is
    # not a "." or a symbol
    new_content = []
    if (content[i - 1][j - 1].isdigit() and content[i - 1][j].isdigit()) or (
        content[i - 1][j].isdigit() and content[i - 1][j + 1].isdigit()
    ):
        new_content.append(content[i - 1][j])
    else:
        new_content.append(content[i - 1][j - 1])
        new_content.append(content[i - 1][j])
        new_content.append(content[i - 1][j + 1])
    if (content[i + 1][j - 1].isdigit() and content[i + 1][j].isdigit()) or (
        content[i + 1][j].isdigit() and content[i + 1][j + 1].isdigit()
    ):
        new_content.append(content[i + 1][j])
    else:
        new_content.append(content[i + 1][j - 1])
        new_content.append(content[i + 1][j])
        new_content.append(content[i + 1][j + 1])
    new_content.append(content[i][j - 1])
    new_content.append(content[i][j + 1])
    # In new content,
    # Check the number of digits in the new content
    for char in new_content:
        if char.isdigit():
            digit_count += 1
    if digit_count == 2:
        return True
    else:
        return False


# Check if the symbol is valid
valid_symbol_indices = []
for i in range(5):
    for j in symbol_indices[i]:
        if valid_symbol(i, j):
            valid_symbol_indices.append([i, j])

# Find all the numbers in the 2 x 2 square of the valid_symbol_indices
valid_number_indices = []
valid_row_numbers = []
for i in range(len(valid_symbol_indices)):
    valid_number_indices.append([])
    row_num = valid_symbol_indices[i][0]
    j = valid_symbol_indices[i][1]
    for k in range(-2, 3):
        if j + k >= 0 and j + k < len(content[i]):
            # Check if j + k is a digit
            if content[i - 1][j + k].isdigit():
                valid_number_indices[-1].append(j + k)
            if content[i][j + k].isdigit():
                valid_number_indices[-1].append(j + k)
            if content[i + 1][j + k].isdigit():
                valid_number_indices[-1].append(j + k)
    valid_number_indices[-1].sort()
    valid_row_numbers.append(row_num)
