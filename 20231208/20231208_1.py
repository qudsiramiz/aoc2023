import numpy as np

# Read the input file
with open("../data/20231208_input.txt", "r") as f:
    # with open("test.txt", "r") as f:
    data = f.read()

# Get rid of the newline at the end
data = data.strip()

# Split the data into a list
data = data.split("\n")

# Get rid of empty strings
data = [x for x in data if x != ""]

instruction_list = data[0]

first_col = []
for i in range(len(data)):
    first_col.append(data[i][0:3])
first_col = np.array(first_col[1:])

destination = "ZZZ"
dest = "VPA"
count = 0
count2 = 0
ind_aaa = np.where(first_col == dest)[0][0] + 1
while dest[-1] != "Z":
    count2 = 0
    for i, instructions in enumerate(instruction_list, start=ind_aaa):
        count2 += 1
        # if i >= 10:
        #     break
        if i == 0 and count == 0:
            dest = data[i + 1][0:3]
            # print(i, dest, count2)
            if dest != destination:
                if instructions == "R":
                    dest = data[i + 1][12:15]
                    print(instructions, dest)
                    if dest == destination:
                        print(f"It took {i + 1} steps to get to {destination}")
                        break
                elif instructions == "L":
                    dest = data[i + 1][7:10]
                    print(instructions, dest)
                    if dest == destination:
                        print(f"It took {i + 1} steps to get to {destination}")
                        break
        else:
            j = np.where(first_col == dest)[0][0] + 1
            dest = data[j][0:3]
            # print(instructions, dest, i, j, count2)
            if dest != destination:
                if instructions == "R":
                    dest = data[j][12:15]
                    if dest == destination:
                        print(f"It took {i + 1} steps to get to {destination}")
                        break
                elif instructions == "L":
                    dest = data[j][7:10]
                    if dest == destination:
                        print(f"It took {i + 1} steps to get to {destination}")
                        break
    count += 1
    # print(dest, count)

print((count - 1) * len(instruction_list) + i - (ind_aaa - 1))
