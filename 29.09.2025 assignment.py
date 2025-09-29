# 1.Write a program to check if a number entered by the user is even or odd.

# 2.Write a program to check whether a number is positive, negative, or zero.

# 3.Write a program that takes two numbers and prints the larger one.

# 4.Ask the user to enter their age and check if they are eligible to vote (age >= 18).

# 5.Check if a number is divisible by both 5 and 11.

# 6.Check if a number is divisible by both 3 and 5.

# 7.Take an amount as input. If it's a multiple of 100 and less than balance, print "Withdrawal Successful", else print reason for failure.

num = eval(input("Enter a number: "))
if num % 2 == 0:
  print(f"{num} is even")
else:
  print(f"{num} is odd")

number = int(input("Enter an integer: "))
str_number = str(number)
if number == 0:
  print(f"{number} is zero")
elif str_number.startswith("-"):
  print(f"{number} is negative")
else:
  print(f"{number} is positive")

a = eval(input("Enter a number:"))
b = eval(input("Enter another number:"))
if a > b:
  print(f"The larger number is {a}")
else:
  print(f"The larger number is {b}")

def compare_two_numbers(a,b):
  a = eval(input("Enter first number: "))
  b = eval(input("Enter second number: "))
  print(max(a,b))

compare_two_numbers(a=5, b=9)

age = int(input("Enter user age: "))
if age >= 18:
  print("eligible to vote")
else:
  print("Ineligible to vote")

a = int(input("Enter a number to check its divisibility with 5 and 11: "))
if a % 5 == 0 and a % 11 == 0:
  print(f"{a} is divisible by 5 and 11. ")
else:
  print(f"{a} is NOT divisible by 5 and 11.")

num = int(input("Enter a number to check its divisibility with 5 and 3: "))
if num % 3 == 0 and num % 5 == 0:
  print(f"{num} is divisible by 5 and 3. ")
else:
  print(f"{num} is NOT divisible by 5 and 3.")

amount = eval(input("Enter the amount to withdraw: "))
acc_balance = 50000
if amount < acc_balance and amount % 100 == 0:
  print("Withdrawal successful.")
else:
  print("Insufficient balance or amount entered incorrectly")
