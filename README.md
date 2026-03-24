# SQL-EDA-Pipeline
this is a pipeline for data cleaning and analysing with help of sql

## Overview
A command-line pipeline that takes a raw CSV, cleans it with Pandas, and runs SQL analysis on it using SQLite. Built as part of my ML engineering roadmap to practice data wrangling and SQL in a production-style project structure."

## Requirements
requirments.txt

## Installation
git clone <url>
pip install -r requirements.txt
python3 run.py --input your_data.csv

## Usage
--input          path to raw CSV (required)
--fill-method    how to fill nulls: mean, median, mode, drop (default: median)
--drop-duplicates remove duplicate rows
--stats          print value counts for categorical columns

## Example Output
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    str    
 4   Sex          891 non-null    str    
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    str    
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    str    
 11  Embarked     889 non-null    str    
dtypes: float64(2), int64(5), str(5)
memory usage: 83.7 KB
None
file size is 61194
       PassengerId    Survived      Pclass         Age       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  714.000000  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642   29.699118    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071   14.526497    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000    0.420000    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000   20.125000    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000   28.000000    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000   38.000000    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000   80.000000    8.000000    6.000000  512.329200

[298 rows x 4 columns]
   PassengerId    Age
0          804   0.42
1          756   0.67
2          470   0.75
3          645   0.75
4           79   0.83
5          631  80.00
6          852  74.00
7           97  71.00
8          494  71.00
9          117  70.50

## License
MIT