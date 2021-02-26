import sqlite3

# Create the database
conn = sqlite3.connect('../data/item_data.db')
c = conn.cursor()

# Create table in database - wrap this in try except to see if the table already exists
c.execute('''CREATE TABLE items (item_name TEXT, post_date DATE, sold_date DATE, post_price INTEGER, 
                                    current_price INTEGER, description TEXT, num_likes INTEGER, num_comments INTEGER, 
                                    num_images INTEGER, url TEXT, refunded BOOLEAN)''')
# Insert a row of data to test
c.execute("INSERT INTO items VALUES ('remove before flight', 'Jul-9-1995', '', 20, 20, 'great tag!', 3, 4, 3, 'someurl.com', false)")
c.execute("INSERT INTO items VALUES ('remove before flight', 'Jul-9-1995', '', 20, 20, 'great tag!', 3, 4, 3, 'someurl.com', false)")

# Save the changes
conn.commit()

# Close connection when done
conn.close()
