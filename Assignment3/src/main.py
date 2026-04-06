import sys
from commonSubsequence import CS


def fail(message: str) -> None:
    print(message)
    sys.exit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail("Usage: python main.py <input_file>")

    try:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip() != ""]
    except OSError:
        fail("Invalid input file path.")

    if not lines:
        fail("Invalid input format.")

    try:
        k = int(lines[0])
    except ValueError:
        fail("Invalid input format. K must be an integer.")

    if k < 1:
        fail("Invalid input format. K must be at least 1.")

    expected_min_lines = 1 + k + 2
    if len(lines) < expected_min_lines:
        fail("Invalid input format. Missing alphabet mappings or strings A/B.")

    v: dict[str, int] = {}
    for i in range(1, k + 1):
        parts = lines[i].split()
        if len(parts) != 2:
            fail("Invalid input format. Each mapping line must be: <char> <value>.")

        ch, raw_value = parts
        if len(ch) != 1:
            fail("Invalid input format. Character key must be a single character.")

        try:
            value = int(raw_value)
        except ValueError:
            fail("Invalid input format. Mapping value must be an integer.")

        v[ch] = value

    a = lines[1 + k]
    b = lines[2 + k]

    for ch in a:
        if ch not in v:
            fail("Invalid input. String A contains character(s) not in alphabet mappings.")

    for ch in b:
        if ch not in v:
            fail("Invalid input. String B contains character(s) not in alphabet mappings.")

    cs = CS(a, b, k, v)
    best_value, subsequence = cs.bottomUp()

    print(best_value)
    print(subsequence)


if __name__ == "__main__":
    main()

    