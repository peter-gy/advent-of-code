def bisect(pattern, low_symbol, high_symbol):
    low, high = (0, 2 ** len(pattern) - 1)
    for symbol in pattern:
        mid = (low + high) // 2
        if symbol == low_symbol:
            high = mid
        elif symbol == high_symbol:
            low = mid + 1
        else:
            raise RuntimeError(f'Unexpected symbol: {symbol}')

    if low != high:
        raise RuntimeError(f'Bisection failed. Low: {low}, High: {high}')

    return low


ROW_PATTERN_LENGTH = 7


def get_seat_id(line):
    row_pattern = line[:ROW_PATTERN_LENGTH]
    col_pattern = line[ROW_PATTERN_LENGTH:]
    return bisect(row_pattern, 'F', 'B') * 8 + bisect(col_pattern, 'L', 'R')


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
