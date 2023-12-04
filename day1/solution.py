import re


def part1(v):
    return sum(int(x[0]+x[-1]) for x in map(lambda l: re.findall("[0-9]",l),v) if x)


def part2(v,d=dict(zip(["one","two","three","four","five","six","seven","eight","nine"],map(str,range(1,10))))):
    return sum(int(x[0]+x[-1]) for x in map(lambda l: [d.get(y,y) for y in re.findall(f"(?=(\d|{'|'.join(d.keys())}))",l)],v) if x)

def main() -> None:
    print("|--Day1--|")
    input_values = open("day1/input.txt", "r").read().split("\n")
    print(f"part1: {part1(input_values)}")
    print(f"part2: {part2(input_values)}")

if __name__ == "__main__":
    main()
