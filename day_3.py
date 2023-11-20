# Odd or even numbers
num = int(input("Pleae enter a number: "))
if num % 2 == 0:
    print(f"The number {num} is even.")
else:
    print(f"The number {num} is odd.")
    
# Python Pizza Deliveries
print("Welcome to Python Pizza Deliveries!")
size = input("WHat size would you like? S, M, L ").upper()
pepperoni = input("Do you like pepperoni? Y/ N ").upper()
extra_cheese = input("Do you want extra cheese? Y/N ").upper()

cost = 0.00
if size == 'S':
    cost += 15
    if pepperoni == 'Y':
        cost += 2
        if extra_cheese == 'Y':
            cost += 1
        else:
            pass
    else:
        pass
elif size == 'M':
    cost += 20
    if pepperoni == 'Y':
        cost += 3
        if extra_cheese == 'Y':
            cost += 1
        else:
            pass
    else:
        pass
elif size == 'L':
    cost += 25
    if pepperoni == 'Y':
        cost += 3
        if extra_cheese == 'Y':
            cost += 1
        else:
            pass
    else:
        pass
else:
    print("Not available!")
print(f"The total cost is $ {cost}.")

# Love Calculator
print("Welcome to the Love Calculator...")
name = input("Please enter your name: ").lower()
crush = input("Please enter the name of your crush: ").lower()
tot = name + crush
t = tot.count('t')
r = tot.count('r')
u = tot.count('u')
e = tot.count('e')

true_count = t + r + u + e

l = tot.count('l')
o = tot.count('o')
v = tot.count('v')

love_count = l + o + v + e

score = str(true_count) + str(love_count)
if int(score) < 10 or int(score) > 90:
    print(f"Your love score is {score}% ")
    print("You go together like coke and mentos...")
elif int(score) > 40 or int(score) < 50:
    print(f"Your love score is {score}% ")
    print("You are alright...")
else:
     print(f"Your love score is {score}% ")


     