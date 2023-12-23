# Coke Machine
# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

# In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

def main():
    balance()


def insert_coin(balance):
    while True:
        coin = int(input("Insert Coin: "))
        if coin == 5 or coin == 10 or coin == 25:
            break
        else:
            amount_due(balance)
            continue
    return coin

def balance():
    balance = 0
    while balance < 50:
        amount_due(balance)
        balance += insert_coin(balance)
    change_owned(balance)

def amount_due(balance):
    print("Amount Due: " + str(50 - balance))

def change_owned(balance):
    print("Change Owed: ", balance - 50, sep="")

main()
