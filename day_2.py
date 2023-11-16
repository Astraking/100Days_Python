# Your life in weeks
#This code assumes the user will be lucky to live until 90

name = input("What is your name?\n")
print(f"Welcome, {name}!")
age = int(input("Please enter your age: \n"))
mene = 90 - age
days = mene * 365
weeks = mene * 52
months = mene * 12
print(f"Dear {name}, you have {mene} years left.\nIt is expressed in months, weeks and days below\n{months} months, {weeks} weeks, {days} days")

# Tip calculator
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? \n"))
tip = int(input("What percent tip would you like to give? 10, 12, 15\n"))
people = int(input("How many people are splitting the bill?:"))
total_bill = round(bill + (tip / 100) * bill, 2 )
pay = round(total_bill / people, 2)
print(f"The total bill is ${total_bill}")
print(f"Each person will pay ${pay}")