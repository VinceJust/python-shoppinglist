# shoppinglist.py

# Empty list to store shopping items
shopping_list = []

def add_item(): # Adds a new item to the shopping list
    item = input("Welchen Artikel möchtest du deiner Liste hinzufügen? ") # Prompt for user to input a shopping item
    shopping_list.append(item) # Adds item to the list
    print(f"Der Artikel '{item}' wurde der Liste hinzugefügt!") # Tells user what item was added to the list 