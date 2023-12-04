import re

max_red = 12
max_green = 13
max_blue = 14

# Read the input file
with open("../data/20231202_input.txt") as f:
    content = f.readlines()

# Remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

# List of all possible ball colors
ball_color_list = ["red", "blue", "green"]

# Create an empty dictionary with game_id as keys
game_dict = {}
power_val = []

for content_val in content[0:]:
    game_id_val = content_val.split(":")[0][5:].zfill(3)
    red_balls = re.findall(r"(\d+) red", content_val)
    green_balls = re.findall(r"(\d+) green", content_val)
    blue_balls = re.findall(r"(\d+) blue", content_val)

    # Convert the list of strings to list of integers
    red_balls = [int(i) for i in red_balls]
    green_balls = [int(i) for i in green_balls]
    blue_balls = [int(i) for i in blue_balls]

    # Find the minimum number of balls in each color
    min_red = max(red_balls)
    min_green = max(green_balls)
    min_blue = max(blue_balls)

    power_val.append(min_red * min_green * min_blue)

print(f"Sum of all the powers: {sum(power_val)}")
