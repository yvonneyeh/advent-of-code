# def get_input():
#     with open("./01/01_input.txt", "r") as file:
#         return [int(line.strip()) for line in file]
#
# def part_1(depth):
#     return sum([1 for i in range(len(depth)) if depth[i] > depth[i-1]])
#
# def part_2(depth):
#     return [(depth[i] + depth[i+1] + depth[i+2]) for i in range(len(depth) - 2)]
#
# print(f'Part 1 = {part_1(get_input())}. Part 2 = part_1(part_2(get_input()))}.')
#


with open("01_input.txt") as file:
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

# # Exercise 2
# increased = 0
# previous_depth = depths[0] + depths[1] + depths[2]
# for i in range(len(depths) - 2):
#     summed_depth = depths[i] + depths[i + 1] + depths[i + 2]
#
#     if summed_depth > previous_depth:
#         increased += 1
#
#     previous_depth = summed_depth
#
# print(increased)
# # 1523
