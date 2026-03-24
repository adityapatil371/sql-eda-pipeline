import argparse
import sys
import pandas as pd
import numpy as np
import sqlite3
conn = sqlite3.connect(':memory:')

class DataAnalyser:
    def __init__(self, args):
        self.input = args.input
        self.conn = sqlite3.connect(':memory:')

    def load(self):
        try:
            self.df = pd.read_csv(self.input)
        except FileNotFoundError:
            print("incorect path")
            sys.exit(1)
        except UnicodeDecodeError:
            print("incorect file type")
            sys.exit(1)
        self.df.to_sql('titanic_data',self.conn)

    def numeric_distribution(self):
        print(self.df.describe())

    def top_correlations(self):
        corr_matrix = self.df.select_dtypes(include='number').corr()
        corr_matrix = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
        print(corr_matrix.unstack().dropna().sort_values().tail(10))

    def run_sql(self,query):
        print(pd.read_sql(query, self.conn))

def main():
    args = user_input()
    analyser = DataAnalyser(args)
    analyser.load()
    analyser.numeric_distribution()
    analyser.top_correlations()
    analyser.run_sql("SELECT AVG(Survived), Pclass FROM titanic_data GROUP BY Pclass")
    analyser.run_sql("SELECT AVG(Survived), Sex FROM titanic_data GROUP BY Sex")
    analyser.run_sql("SELECT AVG(Survived),CASE WHEN Age < 20 THEN '0-20' WHEN Age < 40 THEN '20-40' WHEN Age < 60 THEN '40-60' WHEN Age < 80 THEN '60-80' ELSE '80+' END as AgeGroup FROM titanic_data GROUP BY AgeGroup")
    analyser.run_sql("WITH cte_name AS ( SELECT AVG(Fare) as avg_fare, Pclass FROM titanic_data GROUP BY Pclass ) SELECT avg_fare, titanic_data.Pclass, cte_name.Pclass, Fare FROM titanic_data JOIN cte_name ON titanic_data.Pclass = cte_name.Pclass WHERE Fare > avg_fare")
    analyser.run_sql("SELECT * FROM (SELECT PassengerId, Age FROM titanic_data ORDER BY Age ASC LIMIT 5) UNION ALL SELECT * FROM (SELECT PassengerId, Age FROM titanic_data ORDER BY Age DESC LIMIT 5)")

def user_input() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="add your dataset", required=True)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()