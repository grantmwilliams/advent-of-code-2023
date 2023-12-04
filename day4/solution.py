import re
from math import floor


def part1(v):
    return sum([floor(2**(len(set.intersection(*[set(map(int, g.split())) for g in re.findall(r"Card\s+\d+:\s+(.*?)\s*\|\s*(.*)", t)[0]]))-1)) for t in v])

def part2(input_values: list[str]):
    pass

def main() -> None:
    print("|--Day4--|")
    input_values = open("day4/input.txt", "r").read().split("\n")
    print(f"part1: {part1(input_values)}")
    print(f"part2: {part2(input_values)}")

if __name__ == "__main__":
    main()