## Chocolate House Inventory and Suggestions Management System
This is a simple Python application for managing a fictional chocolate house's:

1. Seasonal flavor offerings
2. Ingredient inventory
3. Customer flavor suggestions and allergy concerns

The application uses SQLite for data storage and Docker for containerized deployment. It includes basic CRUD (Create, Read, Update, Delete) functionality and ensures data integrity with error handling for duplicate entries and edge cases.

## Table of Contents
1. Project Setup
2. Running the Application with Docker
3. Database Structure
4. Functionality
5. Testing and Edge Case Handling
6. Project Structure

## Project Setup
 # Prerequisites
  1. Docker: Make sure Docker is installed and running on your system.
  2. Python (optional): If you want to run the application outside Docker, you’ll need Python 3.9 or higher.

 # Installation
 Clone the repository:
 git clone <your-repo-link>
 cd chocolate_house

## Running the Application with Docker
 Step 1: Build the Docker Image
 From the project root directory, build the Docker image:
 docker build -t chocolate-house .

Step 2: Run the Docker Container
After building the image, start the container:
docker run chocolate-house

This command will run the app.py file in a Docker container, setting up the database and displaying sample data for demonstration.

## Database Structure
The application uses an SQLite database (database.db) that includes the following tables:

seasonal_flavors:

Manages seasonal flavor offerings.
Fields: id (primary key), flavor_name (unique), description.
ingredient_inventory:

Tracks the quantity of ingredients.
Fields: id (primary key), ingredient_name (unique), quantity.
customer_suggestions:

Stores customer flavor suggestions and allergy concerns.
Fields: id (primary key), customer_name, flavor_suggestion, allergy_concern.
Each table has been designed to support basic CRUD operations.

## Functionality
Available Functions in app.py
The following functions are provided in app.py:

add_seasonal_flavor(conn, flavor_name, description):

Adds a new seasonal flavor to the database.
update_ingredient_inventory(conn, ingredient_name, quantity):

Updates the quantity of an ingredient in the inventory.
add_customer_suggestion(conn, customer_name, flavor_suggestion, allergy_concern):

Adds a customer’s flavor suggestion and allergy concern.
view_all_data(conn):

Displays all data from the seasonal_flavors, ingredient_inventory, and customer_suggestions tables.
Sample Data
The main function main() in app.py runs these functions with sample data, which will be displayed in the console when you run the application in Docker.

## Testing and Edge Case Handling
To verify the application works as expected, run it and confirm the output matches the sample data added in the code.

Testing Steps
Adding a Seasonal Flavor:

Run add_seasonal_flavor(conn, "Peppermint Bark", "Holiday flavor with peppermint and chocolate.").
Check the seasonal_flavors table to confirm the flavor has been added.
Updating Ingredient Inventory:

Run update_ingredient_inventory(conn, "Sugar", 50).
Verify the ingredient_inventory table shows the updated quantity for Sugar.
Adding a Customer Suggestion:

Run add_customer_suggestion(conn, "John Doe", "Dark Chocolate Sea Salt", "Peanut allergy").
Confirm that the customer_suggestions table has recorded the suggestion and allergy concern.
Viewing All Data:

Run view_all_data(conn) to display all data from the tables.

## Edge Case Handling
Duplicate Entries:

The application prevents duplicate entries for flavor_name in the seasonal_flavors table and ingredient_name in the ingredient_inventory table.
Attempts to add duplicates will raise an error, which is handled gracefully by the code.
Inventory Update:

The update_ingredient_inventory function can handle both new and existing ingredient entries, updating quantities as necessary.

## Project Structure
.
|-- chocolate_house/
|   |-- app.py               # Main application file
|   |-- database.db          # SQLite database file (created on first run)
|   |-- Dockerfile           # Docker setup file
|   |-- requirements.txt     # Python requirements (empty in this version)
|-- README.md                # Documentation and setup instructions
