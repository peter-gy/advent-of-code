# Pure brute-force. Quick to write, slow to execute. Just Python-stuff... :)
def n_sum(numbers, target_sum, n):
    from itertools import combinations
    return [tpl for tpl in combinations(numbers, n) if sum(tpl) == target_sum]


def solve(numbers, target_sum, n):
    tuples = n_sum(numbers, target_sum, n)
    if not tuples:
        raise RuntimeError(f'No {n}-tuple exists which has a sum of {target_sum}')
    from math import prod
    product = prod(tuples[0])
    print(f'n = {n}, product = {product}')


def one_liner(numbers, target_sum, n):
    from itertools import combinations
    from math import prod
    return prod([tpl for tpl in combinations(numbers, n) if sum(tpl) == target_sum][0])


if __name__ == '__main__':
    numbers = [int(line) for line in open('input.txt', 'r').readlines()]

    solve(numbers, 2020, 2)
    solve(numbers, 2020, 3)

    print(one_liner(numbers, 2020, 2))
    print(one_liner(numbers, 2020, 3))
