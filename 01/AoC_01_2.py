import re

WORD2DIGIT = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}


def main() -> None:
    s = 0
    with open("./data.txt", "r") as file:
        for line in file:
            digits = re.findall(
                r"(?=(\d|one|two|three|four|five|six|seven|eight|nine|zero))", line
            )
            n = "".join(
                [WORD2DIGIT[d] if d.isalpha() else d for d in [digits[0], digits[-1]]]
            )
            s += int(n)
    print(s)


if __name__ == "__main__":
    main()
