import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.txt")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.txt")


"""Copy entry.txt byte-for-byte to the grader output directory.

Reads the one-line entry stored beside this script and writes the exact
bytes to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output when unset), mode
0644. Standard library only; no temporary files, renames, or copies.
"""


def main():
    try:
        with open(SRC, "rb") as source:
            data = source.read()
    except OSError as exc:
        raise SystemExit(f"cannot read entry.txt beside main.py: {exc}")
    if not data:
        raise SystemExit("entry.txt is empty")
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT, "wb") as target:
        target.write(data)
    os.chmod(OUT, 0o644)


if __name__ == "__main__":
    main()
