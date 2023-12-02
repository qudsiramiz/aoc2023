import re

max_red = 12
max_green = 13
max_blue = 14

# Read the input file
with open("input.txt") as f:
    content = f.readlines()

# Remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

# List of all possible ball colors
ball_color_list = ["red", "blue", "green"]

# Create an empty dictionary with game_id as keys
game_dict = {}

for content_val in content[0:]:
    game_id_val = content_val.split(":")[0][5:].zfill(3)
    red_balls = re.findall(r"(\d+) red", content_val)
    green_balls = re.findall(r"(\d+) green", content_val)
    blue_balls = re.findall(r"(\d+) blue", content_val)

    # Convert the list of strings to list of integers
    red_balls = [int(i) for i in red_balls]
    green_balls = [int(i) for i in green_balls]
    blue_balls = [int(i) for i in blue_balls]
    # If max each balls is more than their respective max values, then skip the line
    if (
        max(red_balls) > max_red
        or max(green_balls) > max_green
        or max(blue_balls) > max_blue
    ):
        continue
    else:
        game_dict[game_id_val] = [red_balls[0], green_balls[0], blue_balls[0]]

num_events = []
for key in game_dict.keys():
    num_events.append(int(key))

print(f"Sum of all the valid events: {sum(num_events)}")
