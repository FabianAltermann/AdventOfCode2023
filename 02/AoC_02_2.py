import re
from collections import defaultdict

R = 12
G = 13
B = 14


game_pattern = re.compile(r"(:?Game \d+:)(.*)")
pattern = r"(?:(?P<blue>\d+)\sblue)|(?:(?P<red>\d+)\sred)|(?:(?P<green>\d+)\sgreen)"


def main() -> None:
    solution = 0
    with open("./data.txt", "r") as file:
        for i, line in enumerate(file, start=1):
            red = []
            green = []
            blue = []
            games = re.match(game_pattern, line).groups()[1]
            for game in games.split(";"):
                matches = defaultdict(lambda: 0)  # Default value is None
                for m in re.finditer(pattern, game):
                    for k, v in m.groupdict().items():
                        if v is not None:
                            matches[k] = int(v)
                    red.append(matches["red"])
                    green.append(matches["green"])
                    blue.append(matches["blue"])

            power = max(red) * max(green) * max(blue)
            solution += power
    print(solution)


if __name__ == "__main__":
    main()
