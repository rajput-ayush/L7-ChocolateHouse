import sqlite3
from sqlite3 import Error

# Database connection function
def create_connection():
    try:
        conn = sqlite3.connect("chocolate_house/database.db")
        print("Connection to database established.")
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
    return None

# Function to create necessary tables
def create_tables(conn):
    tables = {
        "seasonal_flavors": """
            CREATE TABLE IF NOT EXISTS seasonal_flavors (
                id INTEGER PRIMARY KEY,
                flavor_name TEXT UNIQUE NOT NULL,
                description TEXT
            );
        """,
        "ingredient_inventory": """
            CREATE TABLE IF NOT EXISTS ingredient_inventory (
                id INTEGER PRIMARY KEY,
                ingredient_name TEXT UNIQUE NOT NULL,
                quantity INTEGER NOT NULL
            );
        """,
        "customer_suggestions": """
            CREATE TABLE IF NOT EXISTS customer_suggestions (
                id INTEGER PRIMARY KEY,
                customer_name TEXT NOT NULL,
                flavor_suggestion TEXT,
                allergy_concern TEXT
            );
        """
    }
    try:
        for table_name, query in tables.items():
            conn.execute(query)
            print(f"Table '{table_name}' created.")
    except Error as e:
        print(f"Error creating tables: {e}")

# Functions to handle CRUD operations
def add_seasonal_flavor(conn, flavor_name, description):
    try:
        conn.execute("INSERT INTO seasonal_flavors (flavor_name, description) VALUES (?, ?)", (flavor_name, description))
        conn.commit()
        print(f"Seasonal flavor '{flavor_name}' added.")
    except Error as e:
        print(f"Error adding flavor: {e}")

def update_ingredient_inventory(conn, ingredient_name, quantity):
    try:
        conn.execute("INSERT OR REPLACE INTO ingredient_inventory (ingredient_name, quantity) VALUES (?, ?)", (ingredient_name, quantity))
        conn.commit()
        print(f"Ingredient '{ingredient_name}' updated with quantity {quantity}.")
    except Error as e:
        print(f"Error updating inventory: {e}")

def add_customer_suggestion(conn, customer_name, flavor_suggestion, allergy_concern):
    try:
        conn.execute("INSERT INTO customer_suggestions (customer_name, flavor_suggestion, allergy_concern) VALUES (?, ?, ?)", 
                     (customer_name, flavor_suggestion, allergy_concern))
        conn.commit()
        print(f"Customer suggestion from '{customer_name}' added.")
    except Error as e:
        print(f"Error adding customer suggestion: {e}")

def view_all_data(conn):
    tables = ["seasonal_flavors", "ingredient_inventory", "customer_suggestions"]
    for table in tables:
        print(f"\nTable: {table}")
        cursor = conn.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

# Main application function
def main():
    conn = create_connection()
    if conn:
        create_tables(conn)
        
        # Adding sample data to demonstrate functionality
        add_seasonal_flavor(conn, "Pumpkin Spice", "A seasonal favorite with pumpkin and spices.")
        update_ingredient_inventory(conn, "Cocoa", 100)
        add_customer_suggestion(conn, "Alice", "Mint Choco", "None")
        
        # View all data
        view_all_data(conn)
        conn.close()

if __name__ == "__main__":
    main()
