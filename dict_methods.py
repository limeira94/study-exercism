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
        if recipe_name in ideas:
            ideas[recipe_name].update(new_ingredients)
        else:
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
    print(update_store_inventory({'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True], 'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]},
            {'Banana': [15, 'Aisle 5', False], 'Apple': [12, 'Aisle 4', False], 'Orange': [1, 'Aisle 4', False], 'Milk': [4, 'Aisle 2', True]}))