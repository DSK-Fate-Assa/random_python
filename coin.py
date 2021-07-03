import random
coin = ["Heads", "Tails"]

player_choice = input("Enter you choice (Heads/Tails): ")

coin_toss = random.choice(coin)

print("You chose:", player_choice)
print("Coin toss shows", coin_toss)

if coin_toss.upper() == player_choice.upper():
    print("You won")
else:
    print("You lost")
