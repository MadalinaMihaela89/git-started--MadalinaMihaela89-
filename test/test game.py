import csv
inventory = {'gold coin': 45, 'arrow': 12,
             'torch': 6, 'dagger': 2, 'rope': 1, 'ruby': 1}
added_items = input("Please add your items with spaces between them: ")


def display_inventory(inventory):
    for key, value in inventory.items():
        print(key, ', ', value)


display_inventory(inventory)


def add_to_inventory(inventory, added_items):

    # added_items_split = added_items.split(" ")
    print(added_items)


add_to_inventory(inventory, added_items)
