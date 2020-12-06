from collections import Counter


def get_yes_any_count(group):
    chars = [ch for ch in group.replace('\n', '')]
    return len(set(chars))


def get_yes_every_count(group):
    group_size = len(group.split('\n'))
    chars = [ch for ch in group.replace('\n', '')]
    return sum([count == group_size for (key, count) in Counter(chars).items()])


def part_1(groups):
    return sum(map(get_yes_any_count, groups))


def part_2(groups):
    return sum(map(get_yes_every_count, groups))


if __name__ == '__main__':
    inp = open('input.txt', 'r').read()
    groups = [group for group in inp.split('\n\n')]
    print('part 1: ', part_1(groups))
    print('part_2: ', part_2(groups))
