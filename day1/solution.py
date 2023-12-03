import re


def part1(input_values: list[str]) -> int:
    return sum(int(x[0]+x[-1]) for x in map(lambda x: re.findall("[0-9]", x), input_values) if x)

def part2(input_values: list[str], digit_patterns = {"one": "1","two": "2","three": "3","four": "4","five": "5","six": "6","seven": "7","eight": "8","nine": "9"}) -> int:
    return sum(int(digit_patterns.get(x[0], x[0])+digit_patterns.get(x[-1], x[-1])) for x in map(lambda x: re.findall(f"(?=(\d|{'|'.join(digit_patterns.keys())}))", x), input_values) if x)

def main() -> None:
    print("|--Day1--|")
    input_values = open("day1/input.txt", "r").read().split("\n")
    print(f"part1: {part1(input_values)}")
    print(f"part2: {part2(input_values)}")

if __name__ == "__main__":
    main()
