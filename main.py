# num_char = len(input("Enteryour name"))

# new_numchar = str(num_char)
# print("your name is " + new_numchar +"character")
# a =float(123)
# print(type(a))
# print(70+ float(123.5))
# print(round(8/6))
# print(round(8/6 , 4))
# print(8//3)
# result = 4/2
# result /= 2
# print(result)

# score = 0 
# score += 1
# print(score)

# score = 0 
# score -= 1
# print(score)

# score = 0 
# score *= 1
# print(score)


# print(type(num_char))

# score = 0
# height = 1.8
# isWinning = True
# #f-string
# print(f"your score is {score}, your height is {height} and your winning is {isWinning}")

print("Welcome to tip calculator")

bill_amount = float(input("What was the total bill?"))
tip_percent = int(input("What percent tip would you like to give? 10,12, or 15?"))
split_ratio = int(input("How many people to split the bill?"))
tip_amount = (bill_amount*(tip_percent/100))/split_ratio
print(f"Each person would pay:{tip_amount}")
