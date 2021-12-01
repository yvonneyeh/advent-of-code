with open("input.txt") as file:
    depths = file.readlines()

# parse inputs
depths = list(map(lambda d: int(d.strip()), depths))

# Exercise 1

# check each depth to see if the previous is smaller
# if so, add 1 to increased counter
increased = 0
previous_depth = depths[0]
for depth in depths:
    if depth > previous_depth:
        increased += 1

    previous_depth = depth

print(increased)
# 1752

# Exercise 2

# keep track of sum of 3 consecutive depths
# loop through all depths (-2)
# increase counter if sum of 3 depths greater than previous
increased2 = 0
previous_depths = depths[0] + depths[1] + depths[2]
for i in range(len(depths) - 2):
    next_depth = depths[i] + depths[i + 1] + depths[i + 2]

    if next_depth > previous_depths:
        increased2 += 1

    previous_depths = next_depth

print(increased2)
# 1781
