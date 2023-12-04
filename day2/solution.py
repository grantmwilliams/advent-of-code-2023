import re
import math


def part1(input_values:list[str], max_color_values={"red":12,"green":13,"blue":14})-> int:
    return sum(int(re.search(r"Game\s(\d+):\s", value).group(1)) for value in input_values if not any(max(map(int, re.findall(f"(\d+)\s{color}", value))) > max_color_values[color] for color in max_color_values))

def part2(input_values: list[str]):
    return sum(math.prod(max(map(int, re.findall(f"(\d+)\s{color}", value))) for color in ["red", "green", "blue"]) for value in input_values)

def main() -> None:
    print("|--Day2--|")
    input_values = open("day2/input.txt", "r").read().split("\n")
    print(f"part1: {part1(input_values)}")
    print(f"part2: {part2(input_values)}")

if __name__ == "__main__":
    main()