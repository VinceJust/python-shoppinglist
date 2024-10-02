# shoppinglist.py

# Empty list to store shopping items
shopping_list = []

# Function to add items to the shopping list
def add_item():
    item = input("Welchen Artikel möchtest du deiner Liste hinzufügen? ") # Prompt for user to input a shopping item
    shopping_list.append(item) # Adds item to the list
    print(f"Der Artikel '{item}' wurde der Liste hinzugefügt!") # Confirms the item was added

# Function to display the shopping list
def show_shoppinglist():
    if shopping_list:  # Corrected variable name
        print("Deine Einkaufsliste:")  # Shows the current shopping list
        for item in shopping_list:
            print(f"- {item}")  # Prints each item in the list
    else:
        print("Deine Einkaufsliste ist leer!")  # Informs the user if the list is empty

# Main function to handle the program flow
def main():
    while True:
        print("\n----- Einkaufsliste -----")
        print("1. Artikel zur Einkaufsliste hinzufügen")
        print("2. Einkaufsliste anzeigen")
        print("3. Programm beenden")
        
        choice = input("Bitte wähle eine Option (1, 2, oder 3): ")  # Gets user input for the choice
        
        if choice == "1":
            add_item()  # Calls the function to add an item
        elif choice == "2":
            show_shoppinglist()  # Calls the function to display the shopping list
        elif choice == "3":
            print("Programm wird beendet! Auf Wiedersehen.")  # Exits the program
            break  # Breaks the loop to end the program
        else:
            print("Ungültige Auswahl. Bitte wähle 1, 2 oder 3.")  # Handles invalid input

# Program entry point
if __name__ == "__main__":
    main()