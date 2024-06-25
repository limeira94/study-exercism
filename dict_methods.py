"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1
    return current_cart


def read_notes(notes):
    note_hash = {}
    for item in notes:
        if item not in note_hash:
            note_hash[item] = notes.count(item)
    return note_hash


def update_recipes(ideas, recipe_updates):
    for recipe_name, new_ingredients in recipe_updates:
        ideas[recipe_name] = new_ingredients
    return ideas


def sort_entries(cart):
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    full_cart = {}
    for item, quantity in cart.items():
        if item in aisle_mapping:
            aisle, refrigeration = aisle_mapping[item]
            full_cart[item] = [quantity, aisle, refrigeration]
    
    sorted_reverse_cart = dict(sorted(full_cart.items(), reverse=True))
    return sorted_reverse_cart    


def update_store_inventory(fulfillment_cart, store_inventory):
    for item, store in fulfillment_cart.items():
        if item in store_inventory:
            quantity, aisle, refrigeration = store_inventory[item]
            if (quantity - store[0]) > 0:
                store_inventory[item] = [quantity - store[0], aisle, refrigeration]
            else:
                store_inventory[item] = ["Out of Stock", aisle, refrigeration]
    return store_inventory


if __name__ == '__main__':
    print(update_recipes({'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
                'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}},
            (('Banana Bread', {'Banana': 4,  'Walnuts': 2, 'Flour': 1, 'Eggs': 2, 'Butter': 1, 'Milk': 2, 'Eggs': 3}),)))