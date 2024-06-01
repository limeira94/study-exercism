"""Functions to keep track and alter inventory."""


def create_inventory(items):
    dict_inv = {}
    for item in items:
        if item is not dict_inv: 
            dict_inv[item] = items.count(item)
    return dict_inv


def add_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] +=1
        else:
            inventory[item] = 1
    return inventory


def decrement_items(inventory, items):
    for item in items:
        if inventory[item] > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return inventory


def list_inventory(inventory):
    list_inv = []
    for key in inventory:
        if inventory[key] > 0:
            list_inv.append((key, inventory[key]))
    return list_inv


if __name__ == '__main__':
    print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))