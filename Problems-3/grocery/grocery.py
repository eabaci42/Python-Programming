# # Grocery List
# # Suppose that you’re in the habit of making a list of items you need from the grocery store.

# # In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.


def main():
    control()


def control():
    grocery_list = {}

    while True:
        try:
            item = get_item()
            grocery_list = dict_operation(grocery_list, item)
        except EOFError:
            print()
            final_operation(grocery_list)
            break


def get_item():
    return input().upper()


def dict_operation(grocery_list, item):
    try:
        if grocery_list[item]:
            grocery_list[item] += 1
    except KeyError:
        grocery_list[item] = 1
    return grocery_list


def final_operation(grocery_list):
    # 1 APPLE
    # 2 BANANA
    # 1 ICE CREAM
    shorted_keys = sorted(grocery_list.keys())
    az_grocery = {k: grocery_list[k] for k in shorted_keys}
    for i in az_grocery:
        print(az_grocery[i], i, sep=" ")


main()
