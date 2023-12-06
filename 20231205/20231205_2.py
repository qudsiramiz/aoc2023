# Read the input file
with open("../data/20231205_input.txt") as f:
    # with open("sample.txt") as f:
    data = f.read()

data = data.split("\n\n")

# Get rid of empty lines
# data = [x for x in data if len(x) >= 2]
seeds = data[0].split()[1:]

maps = data[1:]

for i, m in enumerate(maps):
    maps[i] = m.split("\n")[1:]
    # Get rid of empty values
    maps[i] = [x for x in maps[i] if x != ""]
    maps[i] = [
        [[seed_val, seed_val + range_val], [dest_val, dest_val + range_val]]
        for dest_val, seed_val, range_val in [map(int, x.split()) for x in maps[i]]
    ]

seeds_to_plant_start = seeds[::2]
seeds_to_plant_end = seeds[1::2]
seeds_to_plant = []
for seed_start, seed_end in zip(seeds_to_plant_start, seeds_to_plant_end):
    # seed_value = [int(seed_start), int(seed_end) + int(seed_start)]
    # seeds_to_plant.append(seed_value)
    seeds_to_plant.append([int(seed_start), int(seed_end) + int(seed_start)])


def seed_location(seeds_to_plant, map_list):
    location_val = []
    for map_val in map_list:
        for i, seed in enumerate(seeds_to_plant):
            if seed[0] >= map_val[0][0] and seed[1] <= map_val[0][1]:
                location_val.append(
                    [
                        (seed[0] - map_val[0][0]) + map_val[1][0],
                        (seed[1] - map_val[0][0]) + map_val[1][0],
                    ]
                )
                seed[0] = seed[1]
            elif seed[0] < map_val[0][0] and seed[1] > map_val[0][1]:
                location_val.append(
                    [0 + map_val[1][0], (map_val[0][1] - map_val[0][0]) + map_val[1][0]]
                )
                # Delete seeds_to_plant[i]
                del seeds_to_plant[i]
                seeds_to_plant.insert(i, [seed[0], map_val[0][0]])
                seeds_to_plant.insert(i + 1, [map_val[0][1], seed[1]])

            elif seed[0] >= map_val[0][0] and seed[0] < map_val[0][1]:
                location_val.append(
                    [
                        (seed[0] - map_val[0][0]) + map_val[1][0],
                        (map_val[0][1] - map_val[0][0]) + map_val[1][0],
                    ]
                )
                seed[0] = map_val[0][1]
            elif seed[1] >= map_val[0][0] and seed[1] <= map_val[0][1]:
                location_val.append(
                    [0 + map_val[1][0], (seed[1] - map_val[0][0]) + map_val[1][0]]
                )
                seed[1] = map_val[0][0]

    for seed in seeds_to_plant:
        if seed[0] != seed[1]:
            location_val.append([seed[0], seed[1]])
    return location_val


location_val_2 = seeds_to_plant
for map_val in maps:
    # location_val = seed_location(seeds_to_plant, map_val)
    location_val_2 = sum(
        list(map(seed_location, [location_val_2], [map_val] * len(location_val_2))), []
    )

min_location = min([x[0] for x in location_val_2])

print(min_location)
