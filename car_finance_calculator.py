# Importing file data.csv
# Make sure to update the path as needed

import pandas as pd

df = pd.read_csv('D:\\code\data.csv')

df = df.dropna()

# Getting csv data to lists

superprime = df.loc[1, :].values.tolist()

prime = df.loc[3, :].values.tolist()

nonprime = df.loc[5, :].values.tolist()

subprime = df.loc[7, :].values.tolist()

deep_subprime = df.loc[9, :].values.tolist()


def main():
    print("This is a Auto loan finance calculator. Please enter whole numbers only, no commas needed!")
    
    # trade in and down payment values
    while True:
        try:
            trade_in = float(input("If you have a trade in enter value, if not put 0: "))
        except ValueError:
            print('Numerics only')
            continue
        else:
            break
    
    while True:
        try:
            down_payment = float(input("If you have a down payment enter value, if not put 0: "))
        except ValueError:
            print('Numerics only')
            continue
        else:
            break
            
    while True:
        try:
            credit_score = float(input("Enter credit score number between 300-850: "))
            if (credit_score < 300) or (credit_score > 850):
                print("Invalid number: try again")
                continue
        except ValueError:
            print('Numerics only')
            continue
        else:
            break
main()