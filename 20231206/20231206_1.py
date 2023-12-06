import numpy as np

# Read the file
with open("../data/20231206_input.txt", "r") as f:
    # with open("test.txt", "r") as f:
    data = f.read()

# Get rid of the newline at the end
data = data.strip()

# Split the data into a list
data = data.split("\n")

keys = [x.split(":")[0] for x in data]

race_vals = {}

for i in range(len(data)):
    key_vals = data[i].split(":")[1].split(" ")
    # Remove all the empty strings and conver to integers
    key_vals = [int(x) for x in key_vals if x != ""]
    race_vals[keys[i]] = key_vals

acceleration = 1


def get_distance(time, max_distance):
    times = []
    distances = []
    acceleration = 1
    acceleration_time = np.arange(time + 1)
    travel_time = time - np.arange(time + 1)

    for acceleration_time_val, travel_time_val in zip(acceleration_time, travel_time):
        initial_velocity = acceleration_time_val * acceleration

        distance_covered = initial_velocity * travel_time_val

        if distance_covered > max_distance:
            # print(distance_covered, travel_time_val)
            times.append(travel_time_val)
            distances.append(distance_covered)

    # print(times, distances)
    return times, distances


race_times = race_vals["Time"]
max_distance = race_vals["Distance"]

# Make an empty list of lists of the same length as race_times
times = [None] * len(race_times)
distances = [None] * len(max_distance)

for i, (race_times_val, max_distance_val) in enumerate(
    zip(race_times[:], max_distance[:])
):
    times[i], distances[i] = get_distance(race_times_val, max_distance_val)

ways_to_win = [len(x) for x in times]

# Multiply all the ways to win together
ways_to_win = np.prod(ways_to_win)
print(ways_to_win)
