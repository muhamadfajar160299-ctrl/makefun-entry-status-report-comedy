import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.txt")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.txt")


def main():
    with open(SRC, "rb") as source:
        data = source.read()
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT, "wb") as target:
        target.write(data)


if __name__ == "__main__":
    main()
