def n_sum(numbers, target_sum, n):
    def tuple_has_target_sum(t):
        return sum(t) == target_sum

    from itertools import combinations
    return list(filter(tuple_has_target_sum, list(combinations(numbers, n))))


def solve(numbers, target_sum, n):
    tuples = n_sum(numbers, target_sum, n)
    if not tuples:
        raise RuntimeError(f'No {n}-tuple exists which has a sum of {target_sum}')
    from math import prod
    product = prod(tuples[0])
    print(f'n = {n}, product = {product}')


if __name__ == '__main__':
    numbers = [int(line) for line in open('input.txt', 'r').readlines()]
    solve(numbers, 2020, 2)
    solve(numbers, 2020, 3)
