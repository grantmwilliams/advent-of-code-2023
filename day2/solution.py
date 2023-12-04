import re
from math import prod


def part1(v,m={"red":12,"green":13,"blue":14}):
    return sum(int(re.search(r"Game\s(\d+):\s",x).group(1)) for x in v if not any(max(map(int, re.findall(f"(\d+)\s{c}", x))) > m[c] for c in m))

def part2(v):
    return sum(prod(max(map(int, re.findall(f"(\d+)\s{c}", x))) for c in ["red","green","blue"]) for x in v)

def main() -> None:
    print("|--Day2--|")
    input_values = open("day2/input.txt", "r").read().split("\n")
    print(f"part1: {part1(input_values)}")
    print(f"part2: {part2(input_values)}")

if __name__ == "__main__":
    main()