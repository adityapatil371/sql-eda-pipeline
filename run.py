import argparse
import subprocess
from pathlib import Path
Path("output").mkdir(exist_ok=True)

def main():
    args = user_input()
    cmd = ["python3", "clean.py", "--input", args.input, "--output", "output/cleaned.csv"]
    if args.drop_duplicates:
        cmd.append("--drop-duplicates")
    if args.stats:
        cmd.append("--stats")
    cmd.extend(["--fill-method", args.fill_method])
    subprocess.run(cmd)
    subprocess.run(["python3", "analyse.py", "--input", "output/cleaned.csv"])

def user_input() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="add your dataset", required=True)
    parser.add_argument("--fill-method", help="add what to fill in blanks", choices=["mean", "median", "mode", "drop"], default="median")
    parser.add_argument("--drop-duplicates", help="add if true", action='store_true')
    parser.add_argument("--stats", help="add if stats analysis is needed", action='store_true')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()