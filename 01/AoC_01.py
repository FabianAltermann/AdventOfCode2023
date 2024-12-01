import re


def main() -> None:
    # pattern = re.compile(r"^[a-z]*\d+[a-z]\d[a-z]*$", re.IGNORECASE)
    pattern = re.compile(r"\d", re.IGNORECASE)
    s = 0
    with open("./data.txt", "r") as file:
        for line in file:
            if matches := pattern.findall(line):
                s += int(f"{matches[0]}{matches[-1] if len(matches)>1 else matches[0]}")
    print(s)


if __name__ == "__main__":
    main()
