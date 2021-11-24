print("Welcome to tip calculator")

bill_amount = float(input("What was the total bill? $"))
tip_percent = int(input("What percent tip would you like to give? 10,12, or 15? "))
split_ratio = int(input("How many people to split the bill? "))
tip_amount = round((bill_amount*(tip_percent/100) + bill_amount)/split_ratio , 2)
print(f"Each person would pay:${tip_amount}")

