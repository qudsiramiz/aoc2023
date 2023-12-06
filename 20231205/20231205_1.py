import numpy as np
import re

# Read the input file
with open("../data/20231205_input.txt") as f:
    # with open("sample.txt") as f:
    data = f.read()

data = data.split("\n")
data = [x.split(":") for x in data]
# Get rid of empty lines
# data = [x for x in data if len(x) >= 2]
seeds = data[0][0]
seeds_val = data[0][1].strip().split(" ")
seeds_val = [int(x) for x in seeds_val]

# Remove the first line from the data
new_data = data[1:]
new_data = [x for x in new_data if x[0] != ""]

maps = {}
row_num = []
# Find the row numbers with letters
for i, x in enumerate(new_data):
    if re.search("[a-zA-Z]", x[0]):
        row_num.append(i)
        # Add the character to the dictionary as a key
        maps[x[0]] = x[1].strip().split(" ")

# Add the value of new_data from the row_num to the dictionary
for i in range(len(row_num)):
    if i == len(row_num) - 1:
        maps[list(maps.keys())[i]] = new_data[row_num[i] + 1 :]
    else:
        maps[list(maps.keys())[i]] = new_data[row_num[i] + 1 : row_num[i + 1]]

# Convert the values to integers
map_new = {}
for key in maps.keys():
    key_values = maps[key]
    map_new[key] = []
    for x in key_values:
        key_values_rows = x[0].strip().split(" ")
        key_values_rows = [int(x) for x in key_values_rows]
        map_new[key].append(key_values_rows)

# Convert the values to numpy arrays
for key in map_new.keys():
    map_new[key] = np.array(map_new[key])

# Get the second column of each row
# map_new_seed_to_soil = map_new["seed_to_soil"][1]


def get_location(var1, var2, key):
    """
    Parameters
    ----------
    var1 : list
        List of values.
    var2 : dict
        Dictionary of values.
    key : str
        Key of the dictionary.

    Returns
    -------
    location_val : list
        List of values.

    Example
    -------
    >>> var1 = [1, 2, 3, 4, 5]
    >>> var2 = {"a": [[1, 2, 3], [4, 5, 6]]}
    >>> key = "a"
    >>> get_location(var1, var2, key)
    [2, 5]
    """
    destination_in_map = var2[key][:, 0]
    source_in_map = var2[key][:, 1]
    range_in_map = var2[key][:, 2]

    location_val = []
    for seed in var1:
        found_location = False
        for destination_in_map_val, source_in_map_val, range_in_map_val in zip(
            destination_in_map, source_in_map, range_in_map
        ):
            # Check if the seed is in the range of source_in_map_val to source_in_map_val +
            # range_in_map_val
            if source_in_map_val <= seed <= source_in_map_val + range_in_map_val:
                diff = seed - source_in_map_val
                # print(f"diff: {diff}")
                # print(f"destination_in_map_val: {destination_in_map_val}")
                location_val.append(destination_in_map_val + diff)
                found_location = True
                break
        if not found_location:
            location_val.append(seed)

    # print(f"location_val: {location_val}")
    return location_val


# Get the soil location for each seed
soil_location = get_location(seeds_val, map_new, "seed-to-soil map")

# Get the fertilizer location for each seed
fertilizer_location = get_location(soil_location, map_new, "soil-to-fertilizer map")

# Get the water location for each seed
water_location = get_location(fertilizer_location, map_new, "fertilizer-to-water map")

# Get the light location for each seed
light_location = get_location(water_location, map_new, "water-to-light map")

# Get the temperature location for each seed
temperature_location = get_location(light_location, map_new, "light-to-temperature map")

# Get the humidity location for each seed
humidity_location = get_location(
    temperature_location, map_new, "temperature-to-humidity map"
)

# Get the location for each seed
location = get_location(humidity_location, map_new, "humidity-to-location map")


# Ge the minimum value of the location
min_location = min(location)
print(f"min_location: {min_location}")
