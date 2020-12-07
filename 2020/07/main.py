from typing import Dict, Tuple
import re

WeightedNode = Tuple[str, Dict[str, int]]  # bag_color, inner_bags
WeightedGraph = Dict[str, Dict[str, int]]

outer_bag_pattern = r'([a-z]+ [a-z]+) bags contain (.+)'  # (color) bags contain (inner_bag_pattern)
inner_bag_pattern = r'(\d+) ([a-z]+ [a-z]+) bag'  # (inner_count) (inner_color) bag
special_bag_color = 'shiny gold'


def parse_line_to_bag_node(line) -> WeightedNode:
    color, inner_bags = re.findall(outer_bag_pattern, line)[0]
    inner_count_color_tuples = re.findall(inner_bag_pattern, inner_bags)
    return color, {inner_color: int(inner_count) for (inner_count, inner_color) in inner_count_color_tuples},


def parse_lines_to_bag_graph(lines) -> WeightedGraph:
    return {color: inner_bags for color, inner_bags in map(parse_line_to_bag_node, lines)}


lines = [line.strip() for line in open('input.txt', 'r').readlines()]
graph: WeightedGraph = parse_lines_to_bag_graph(lines)


def special_bag_fits_into_bag(bag_color) -> bool:
    return True if special_bag_color in graph[bag_color] else any(map(special_bag_fits_into_bag, graph[bag_color]))


def inner_bags_count(bag_color):
    return 1 + sum(inner_count * inner_bags_count(inner_color) for inner_color, inner_count in graph[bag_color].items())


def part_1():
    return sum(map(special_bag_fits_into_bag, graph.keys()))


def part_2():
    return inner_bags_count(special_bag_color) - 1  # subtract 1, as the special bag itself should not be counted


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
