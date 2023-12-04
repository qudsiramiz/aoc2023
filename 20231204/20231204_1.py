# Read the input file
with open("../data/20231204_input.txt") as f:
    content = f.readlines()

# Remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

# Part 1
