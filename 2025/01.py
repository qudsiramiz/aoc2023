import numpy as np

dat = np.loadtxt("data/input_01.txt", "str")

n_step = np.zeros(len(dat), dtype=int)
for i, x in enumerate(dat):
    direction = -1 if x[0] == "L" else 1
    n_step[i] = direction * int(x[1:])

counter = 0
position = 50
for step in n_step:
    prev_position = position
    position += step
    if step > 0:
        counter += (position // 100) - (prev_position // 100)
    elif step < 0:
        counter += ((prev_position - 1) // 100) - ((position - 1) // 100)

print(counter)
