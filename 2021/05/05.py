def open_file(input_file):
    with open(input_file, "r") as file:
        rows = [row.rstrip() for row in file]
        lines = [
            [
                [int(num) for num in coord.split(",")]
                for coord in row.split(" -> ")
            ] for row in rows
        ]
    return lines


def count_overlaps(vent_positions):
    overlaps = 0
    for points in vent_positions.values():
        if points > 1:
            overlaps += 1
    return overlaps


def part_one(input_file):

    # Part 1
    lines = open_file(input_file)
    vent_positions = {}
    for line in lines:
        [x1, y1], [x2, y2] = line
        if x1 == x2:
            small_y = min(y1, y2)
            big_y = max(y1, y2)
            for y in range(small_y, big_y + 1):
                position = (x1, y)
                if position in vent_positions:
                    vent_positions[position] += 1
                else:
                    vent_positions[position] = 1
        elif y1 == y2:
            small_x = min(x1, x2)
            big_x = max(x1, x2)
            for x in range(small_x, big_x + 1):
                position = (x, y1)
                if position in vent_positions:
                    vent_positions[position] += 1
                else:
                    vent_positions[position] = 1

    overlaps = count_overlaps(vent_positions)

    print("Part 1")
    print("There are", overlaps, "points where at least two lines overlap")

    return overlaps

def part_two(input_file):

    lines = open_file(input_file)
    vent_positions = {}
    for line in lines:
        [x1, y1], [x2, y2] = line
        small_x = min(x1, x2)
        big_x = max(x1, x2)
        small_y = min(y1, y2)
        big_y = max(y1, y2)
        x_delta = big_x - small_x
        y_delta = big_y - small_y
        if x1 == x2:
            for y in range(small_y, big_y + 1):
                positions = (x1, y)
                if positions in vent_positions:
                    vent_positions[positions] += 1
                else:
                    vent_positions[positions] = 1
        elif y1 == y2:
            for x in range(small_x, big_x + 1):
                positions = (x, y1)
                if positions in vent_positions:
                    vent_positions[positions] += 1
                else:
                    vent_positions[positions] = 1
        elif x_delta == y_delta:
            x_dir_coeff = 1 if x2 > x1 else -1
            y_dir_coeff = 1 if y2 > y1 else -1
            for i in range(x_delta + 1):
                positions = (x1 + i * x_dir_coeff, y1 + i * y_dir_coeff)
                if positions in vent_positions:
                    vent_positions[positions] += 1
                else:
                    vent_positions[positions] = 1

    overlaps = count_overlaps(vent_positions)
    print("Part 2")
    print("There are", overlaps, "points where at least two lines overlap")
    return overlaps


part_one_answer = part_one("input.txt")
part_two_answer = part_two("input.txt")

print(f"Answer #1 = {part_one_answer}")    #6572
print(f"Answer #2 = {part_two_answer}")    #21466
