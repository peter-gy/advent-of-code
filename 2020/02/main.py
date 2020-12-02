from collections import namedtuple
import re

LineData = namedtuple('LineData', 'low up ch pwd')


# 9-11 p: pppppppppxblp
def get_linedata(line):
    match = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    return LineData(low=int(match.group(1)),
                    up=int(match.group(2)),
                    ch=match.group(3),
                    pwd=match.group(4))


def part1_predicate(line):
    low, up, ch, pwd = get_linedata(line)
    return low <= pwd.count(ch) <= up


def part2_predicate(line):
    low, up, ch, pwd = get_linedata(line)
    return (pwd[low - 1] == ch) ^ (pwd[up - 1] == ch)


if __name__ == '__main__':
    lines = open('input.txt', 'r').readlines()
    print(sum([part1_predicate(line) for line in lines]))
    print(sum([part2_predicate(line) for line in lines]))
