def open_file(input_file):
    with open(input_file) as file:
        lines = file.readlines()
    return lines

def part_one(input_file):

    directions = open_file(input_file)
    horizontal_position = 0
    depth = 0

    for line in directions:
        if "forward" in line:
            x = int(line.strip("forward"))
            horizontal_position += x
        elif "down" in line:
            x = int(line.strip("down"))
            depth += x
        elif "up" in line:
            x = int(line.strip("up"))
            depth -= x

    return horizontal_position * depth


def part_two(input_file):

    directions = open_file(input_file)
    horizontal_position = 0
    depth = 0
    aim = 0

    for line in directions:
        if "down" in line:
            x = int(line.strip("down"))
            aim += x
        elif "up" in line:
            x = int(line.strip("up"))
            aim -= x
        elif "forward" in line:
            x = int(line.strip("forward"))
            horizontal_position += x
            depth += aim * x

    return horizontal_position * depth


part_one_answer = part_one("input.txt")
part_two_answer = part_two("input.txt")

print(f"Answer #1 = {part_one_answer}") #1604850
print(f"Answer #2 = {part_two_answer}") #1685186100
