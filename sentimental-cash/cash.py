from cs50 import get_float

# user input
while True:
    decCents = get_float("Change owed: ")
    if decCents > 0:
        break


# converting decimal to cents
cents = decCents * 100

# number of quarters
quarters = cents // 25
cents = cents - quarters * 25

# number of dimes
dimes = cents // 10
cents = cents - dimes * 10

# number of nickels
nickels = cents // 5
cents = cents - nickels * 5

# number of pennies
pennies = cents // 1
cents = cents - pennies * 1

# total number of coins
coins = quarters + dimes + nickels + pennies
coins = int(coins)

# print the total number of coins
print(coins)