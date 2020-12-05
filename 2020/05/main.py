from functools import reduce

ROW_PATTERN_LENGTH = 7
row_symbol_to_binary_dict = {
    'F': '0',
    'B': '1'
}

col_symbol_to_binary_dict = {
    'L': '0',
    'R': '1'
}


def get_seat_id(line):
    row_pattern = line[:ROW_PATTERN_LENGTH]
    col_pattern = line[ROW_PATTERN_LENGTH:]
    row_binary_str = reduce(lambda acc, ch: acc.replace(ch, row_symbol_to_binary_dict[ch]), row_pattern, row_pattern)
    col_binary_str = reduce(lambda acc, ch: acc.replace(ch, col_symbol_to_binary_dict[ch]), col_pattern, col_pattern)
    return int(row_binary_str, 2) * 8 + int(col_binary_str, 2)


def get_sorted_seat_ids(lines):
    return sorted([get_seat_id(line) for line in lines])


def part_1(lines):
    return get_sorted_seat_ids(lines)[-1]


def part_2(lines):
    ids = get_sorted_seat_ids(lines)
    expected_sum = sum(range(ids[0], ids[-1] + 1))
    actual_sum = sum(ids)
    return expected_sum - actual_sum


if __name__ == '__main__':
    lines = [line.strip() for line in open('input.txt', 'r').readlines()]
    print('part 1: ', part_1(lines))
    print('part_2: ', part_2(lines))
