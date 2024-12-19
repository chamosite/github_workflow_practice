from pathlib import Path

import pandas as pd


def main():
    try:
        config = Path("config.txt")
        with open(config, "r") as f:
            s = f.read()
        print(s)
        df = pd.DataFrame([s])
        df.to_csv("config.csv")
    except Exception as e:
        print(f"{e}")
    finally:
        input("Please press enter key.")


if __name__ == "__main__":
    main()
