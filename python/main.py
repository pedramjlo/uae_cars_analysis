import pandas as pd
import sqlite3

# Step 1: Create a connection to the SQLite database
conn = sqlite3.connect('uae_cars.db')  # This will create a new database file named 'example.db'

# Step 2: Create a cursor object
cur = conn.cursor()

# Step 3: Execute SQL commands
# Create a table
cur.execute('''

CREATE TABLE IF NOT EXISTS uae_cars (
    id INTEGER PRIMARY KEY,
    Make VARCHAR(50),
    Model VARCHAR(50),
    Year INT,
    Price INT,
    Mileage INT,
    Body_Type VARCHAR(50),
    Cylinders INT,
    Transmission VARCHAR(50),
    Fuel_Type VARCHAR(50),
    Color VARCHAR(50),
    Location VARCHAR(50),
    Description VARCHAR(100) 
)
''')


# Step 4: Commit changes
conn.commit()


# Step 5: Read the CSV file using Pandas
df = pd.read_csv('/Users/pedramjalali/Documents/data_analysis/uae_cars_analysis/dataset/cleaned/cleaned_uae_cars.csv')



# Step 6: Load data into the SQLite database table
df.to_sql('uae_cars', conn, if_exists='append', index=False)



# Step 5: Close the connection
conn.close()
