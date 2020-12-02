from collections import namedtuple
import re

count = 0

LineData = namedtuple('LineData', 'low up ch pwd')


# 9-11 p: pppppppppxblp
def get_linedata(line):
    match = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    return LineData(low=int(match.group(1)),
                    up=int(match.group(2)),
                    ch=match.group(3),
                    pwd=match.group(4))


def part1_predicate(line):
    ld = get_linedata(line)
    return ld.low <= ld.pwd.count(ld.ch) <= ld.up


def part2_predicate(line):
    ld = get_linedata(line)
    return (ld.pwd[ld.low - 1] == ld.ch) ^ (ld.pwd[ld.up - 1] == ld.ch)


if __name__ == '__main__':
    lines = open('input.txt', 'r').readlines()
    print(sum([part1_predicate(line) for line in lines]))
    print(sum([part2_predicate(line) for line in lines]))
