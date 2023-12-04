import numpy as np

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
    points.append(count)


# Number of cards
number_cards = np.ones(len(points))

for i, (point_value, number_cards_val) in enumerate(zip(points, number_cards)):
    if point_value == 0:
        continue
    else:
        for k in range(int(number_cards_val)):
            for j in range(point_value):
                number_cards[int(i + j + 1)] += 1

# Add up all the number_cards
print(sum(number_cards))
