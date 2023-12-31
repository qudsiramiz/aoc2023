# Read the input file
with open("../data/20231204_input.txt") as f:
    content = f.readlines()

# Remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

# Part 1
points = []
for line in content:
    w_numbers = line.split(":")[1].split("|")[0].split(" ")
    # Get rid of empty strings
    w_numbers = list(filter(None, w_numbers))

    m_numbers = line.split(":")[1].split("|")[1].split(" ")
    # Get rid of empty strings
    m_numbers = list(filter(None, m_numbers))

    # Check how many m_numbers are in w_numbers
    count = 0
    for number in m_numbers:
        if number in w_numbers:
            count += 1
    if count > 0:
        points.append(2 ** (count - 1))

# Add up all the winning values
print(sum(points))

