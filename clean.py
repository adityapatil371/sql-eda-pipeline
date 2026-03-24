import argparse
import pandas as pd
from pathlib import Path

class DataCleaner:
    def __init__(self,args)-> None:
        self.input = args.input
        self.output = args.output
        self.fill_method = args.fill_method
        self.drop_duplicates = args.drop_duplicates
        self.stats = args.stats

    def load(self):
        try:
            self.df = pd.read_csv(self.input)
        except FileNotFoundError:
            print("incorect path")
            sys.exit(1)
        except UnicodeDecodeError:
            print("incorect file type")
            sys.exit(1)

    def report(self):
        print(self.df.info())
        print(f"file size is {Path(self.input).stat().st_size}")
        if self.stats:
            print(self.df.describe())
            for col in self.df.select_dtypes(include='str').columns:
                print(self.df[col].value_counts())

    def clean(self):
        self.df = self.df.convert_dtypes()
        if self.fill_method == "mean":
            self.df = self.df.fillna(self.df.mean())
        elif self.fill_method == "median":
            self.df = self.df.fillna( self.df.select_dtypes(include='number').median())
        elif self.fill_method == "mode":
            self.df = self.df.fillna(self.df.mode())
        else:
            self.df = self.df.dropna()
        if self.drop_duplicates:
            self.df = self.df.drop_duplicates()

    def save(self):
        self.df.to_csv(self.output, index=False)

def main():
    args = user_input()
    cleaner = DataCleaner(args)
    cleaner.load()
    cleaner.report()
    cleaner.clean()
    cleaner.save()

def user_input() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="add your dataset", required=True)
    parser.add_argument("--output", help="add your output path", required=True)
    parser.add_argument("--fill-method", help="add what to fill in blanks", choices=["mean", "median", "mode", "drop"], default="median")
    parser.add_argument("--drop-duplicates", help="add if true", action='store_true')
    parser.add_argument("--stats", help="add if stats analysis is needed", action='store_true')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()