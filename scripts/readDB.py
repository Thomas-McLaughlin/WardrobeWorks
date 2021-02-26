import sqlite3

# Connect to the database
conn = sqlite3.connect('../data/item_data.db')
c = conn.cursor()

# Print an item from the database to verify it exists
c.execute('SELECT * FROM items')
print(c.fetchall())