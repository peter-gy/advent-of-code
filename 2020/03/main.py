import math


def count_trees(lines, right, down):
    r = down
    c = right
    trees = 0
    while r < len(lines):
        row = lines[r]
        if c + right >= len(row):
            row *= math.ceil((c + right) / len(row))
        symbol = row[c]
        if symbol == '#':
            trees += 1
        c += right
        r += down
    return trees


if __name__ == '__main__':
    lines = [l.strip() for l in open('input.txt', 'r').readlines()]

    print('part 1:', count_trees(lines, 3, 1))

    product = math.prod([count_trees(lines, *steps) for steps in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]])
    print('part 2:', product)
