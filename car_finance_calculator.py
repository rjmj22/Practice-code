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
    
    # new or used, trade in, down payment, credit score and overall car values:

    while True:
        try:
            condition = float(input("If vehicle is New, enter 1. If used enter 2: "))
            if (condition < 1) or (condition > 2):
                print("Invalid number: try again")
                continue
        except ValueError:
            print('1 or 2 only:')
            continue
        else:
            break

    
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
    
    
    while True:
        try:
            auto_price = float(input("Enter the total price of the vehicle: "))
        except ValueError:
            print('Numerics only')
            continue
        else:
            break

# matching credit score to rate

    if credit_score >= 781 and condition == 1:
        rate = superprime[2]
    elif credit_score >= 661 and condition == 1:
        rate = prime[2]
    elif credit_score >= 601 and condition == 1:
        rate = nonprime[2]
    elif credit_score >= 501 and condition == 1:
        rate = subprime[2]
    elif credit_score <= 500 and condition == 1:
        rate = deep_subprime[2]
    elif credit_score >= 781 and condition == 2:
        rate = superprime[3]
    elif credit_score >= 661 and condition == 2:
        rate = prime[3]
    elif credit_score >= 601 and condition == 2:
        rate = nonprime[3]
    elif credit_score >= 501 and condition == 2:
        rate = subprime[3]
    elif credit_score <= 500 and condition == 2:
        rate = deep_subprime[3]

# figuring our principal and interest rate by year
  
    principal = (auto_price - (down_payment + trade_in))
    
    int3 = (principal * rate * 3)
    int4 = (principal * rate * 4)
    int5 = (principal * rate * 5)
    int6 = (principal * rate * 6)
    int7 = (principal * rate * 7)

    print("The monthly payment for 36 months is: ",int((principal + int3) / 36 ))
    print("The monthly payment for 48 months is: ",int((principal + int4) / 48 ))
    print("The monthly payment for 60 months is: ",int((principal + int5) / 60 ))


main()