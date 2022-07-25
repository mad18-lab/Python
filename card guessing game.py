import random
cards = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10']

print("WELCOME TO THE GAME")
name = str(input("ENTER YOUR NAME: "))
print("\nGOOD LUCK ", name, "!")
print("\nTHE CARDS ARE AS FOLLOWS: ")

for card in cards:
    print(card, end=" ")

tries = 5
print("\nThe number of given tries: ", tries)

guess = random.choice(cards)

while tries != 0:
    if guess != 0:
        tries = tries - 1
        choice = input("\n\nEnter your choice: ")
        if choice != guess:
            print("Your choice ", choice, " is wrong. Keep going!")
            continue
        else:
            print("Your choice ", choice, " is right. You win!")
            break
print("You have exhausted your tries. Game over.")
