# Heads or tails
import random 
flip = random.randint(0, 2)
if flip == 0:
    print("Tails")
else:
    print("Heads")

# # Bill roulette
names_string = "Angela, Jack, Ryan, Teddy, Narh"
names = names_string.split(", ")
print(names)
payer = random.choice(names)
print(f"{payer} is going to pay the bill.")

# Teasure map
row1 = ["⬜","⬛","⬜"]
row2 = ["⬛","⬜","⬛"]
row3 = ["⬜","⬛","⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Separate with a comma: ")
i, j = position.split(",")
i, j = int(i), int(j)
print(i, j)
map[i][j] = 'x'
print(f"{row1}\n{row2}\n{row3}")

# Rock Paper Scissors
print("Welcome to Rock, Paper, Scissors!")
user = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
computer = random.randint(0,2)
print(f"Computer chose {computer}")
if user not in range(0, 3):
    print("Invalid number!")
elif computer > user:
    print("Computer wins!")
elif computer == 0 and user == 2:
    print("Computer wins!")
elif computer == 2 and user == 0:
    print("User wins!")
elif computer  == user:
    print("It is a draw!")
elif computer <  user:
    print("User wins!")



     
