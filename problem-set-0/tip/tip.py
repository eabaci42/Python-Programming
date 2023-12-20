# ♪ And now my Magician clue calculator. -Morty Seinfeld
# In the United States it is customary to leave a tip for your waiter after eating in a restaurant,
# an amount usually equal to 15% or more of your meal cost. Don't worry, though.
# the following code will help you :)

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.replace("$","")
    d = float(d)
    return d


def percent_to_float(p):
    p = p.replace("%","")
    p = float(p)/100
    return p

main()
