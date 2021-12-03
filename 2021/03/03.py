def open_file(input_file):
    with open(input_file) as file:
        return [[int(column) for column in row] for row in file]

def part_one(input_file):

    matrix = open_file(input_file)
    transposed_matrix = zip(*matrix)
    summed_rows = map(sum, transposed_matrix)
    majority = list(map(lambda s: s > len(matrix)//2, summed_rows))

    gamma   = ''.join('1' if b else '0' for b in majority)
    epsilon = ''.join('0' if b else '1' for b in majority)

    power_consumption = gamma * epsilon

    return power_consumption


def part_two(input_file):

    pass


part_one_answer = part_one("input.txt")
part_two_answer = part_two("input.txt")

print(f"Answer #1 = {part_one_answer}")    #
print(f"Answer #2 = {part_two_answer}")    #
