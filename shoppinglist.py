import sqlite3

# function to connect with the databank
def connect_db():
    conn = sqlite3.connect('groceries.db')
    cursor = conn.cursor()
    return conn, cursor

# function for creating a table
def create_table():
    conn, cursor = connect_db()
    cursor.execute('''CREATE TABLE IF NOT EXISTS groceries (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   amount INTEGER NOT NULL,
                   price REAL NOT NULL
               )''')
    conn.commit()
    conn.close()

# function for adding a new item to the shopping list
def add_item():
    item = input("Welchen Artikel möchtest du deiner Liste hinzufügen? ").strip()
    amount = input("Wie viele Einheiten möchtest du hinzufügen? ").strip()
    price = input("Was ist der Preis pro Einheit? ").strip()
    
    if item and amount.isdigit() and price.replace('.', '', 1).isdigit():
        amount = int(amount)
        price = float(price)
        conn, cursor = connect_db()
        cursor.execute("INSERT INTO groceries (name, amount, price) VALUES (?, ?, ?)", (item, amount, price))
        conn.commit()
        conn.close()
        print(f"Der Artikel '{item}' wurde der Liste hinzugefügt!")
    else:
        print("Ungültige Eingabe. Bitte stelle sicher, dass Menge eine Zahl und Preis eine gültige Dezimalzahl ist.")

# read function for reading out the shopping list
def show_shoppinglist():
    conn, cursor = connect_db()
    cursor.execute("SELECT * FROM groceries")
    results = cursor.fetchall()
    if results:
        print("Deine Einkaufsliste:")
        for row in results:
            print(f"- ID: {row[0]}, Artikel: {row[1]}, Menge: {row[2]} Einheiten, Preis: {row[3]} EUR pro Einheit")
    else:
        print("Deine Einkaufsliste ist leer!")
    conn.close()

# update function for editing an entry
def update_item():
    show_shoppinglist()
    item_id = input("Gib die ID des Artikels ein, den du bearbeiten möchtest: ").strip()
    
    if item_id.isdigit():
        new_name = input("Neuer Name des Artikels: ").strip()
        new_amount = input("Neue Menge: ").strip()
        new_price = input("Neuer Preis pro Einheit: ").strip()
        
        if new_name and new_amount.isdigit() and new_price.replace('.', '', 1).isdigit():
            new_amount = int(new_amount)
            new_price = float(new_price)
            conn, cursor = connect_db()
            cursor.execute("UPDATE groceries SET name = ?, amount = ?, price = ? WHERE id = ?", (new_name, new_amount, new_price, item_id))
            conn.commit()
            conn.close()
            print(f"Der Artikel mit der ID {item_id} wurde aktualisiert!")
        else:
            print("Ungültige Eingabe. Bitte überprüfe deine Angaben.")
    else:
        print("Ungültige ID.")

# delete function for deleting entries
def delete_item():
    show_shoppinglist()
    item_id = input("Gib die ID des Artikels ein, den du löschen möchtest: ").strip()
    
    if item_id.isdigit():
        conn, cursor = connect_db()
        cursor.execute("DELETE FROM groceries WHERE id = ?", (item_id,))
        conn.commit()
        conn.close()
        print(f"Der Artikel mit der ID {item_id} wurde gelöscht!")
    else:
        print("Ungültige ID.")

# main menu for CRUD operation
def main():
    create_table()  # creates table

    while True:
        print("\n--- Einkaufsliste ---")
        print("1. Artikel hinzufügen")
        print("2. Einkaufsliste anzeigen")
        print("3. Artikel bearbeiten")
        print("4. Artikel löschen")
        print("5. Beenden")

        choice = input("Wähle eine Option (1-5): ").strip()

        if choice == "1":
            add_item()  # adds an item
        elif choice == "2":
            show_shoppinglist()  # shows shopping list
        elif choice == "3":
            update_item()  # edits an item
        elif choice == "4":
            delete_item()  # deletes item
        elif choice == "5":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Eingabe, bitte wähle eine Option zwischen 1 und 5.")

# starts the programm
if __name__ == "__main__":
    main()