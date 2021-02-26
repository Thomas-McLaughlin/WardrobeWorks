import sqlite3
from sqlite3 import OperationalError
import sys

"""
This file is for first setup, so that the relevant databases can be created.
"""

'''
Create item_data db with following fields:
Post Date               [DATE]
Sold Date               [DATE]
post_price              [INTEGER]
current_price           [INTEGER]
description             [TEXT]
Number of Likes         [INT]
Number of Comments      [INT]
URL to Listing          [STRING/URI]
num_images              [INTEGER]
Refunded (True/False)   [BOOLEAN]
'''
# Create the item_data.db
conn = sqlite3.connect('../data/item_data.db')
c = conn.cursor()

# Try to create the db and table, otherwise it already exists
try:
    print("Creating item_data db...")
    c.execute('''CREATE TABLE items (item_name TEXT, post_date DATE, sold_date DATE, post_price INTEGER, 
                                    current_price INTEGER, description TEXT, num_likes INTEGER, num_comments INTEGER, 
                                    num_images INTEGER, url TEXT, refunded INTEGER)''')
    print("DB created")
except OperationalError:
    print(sys.exc_info()[1])

print("Testing Insert...")
# Insert a row of data to test
# As needed for SQL Insert
test_items = ["('remove before flight', 'Jul-9-1995', '', 20, 20, 'great tag!', 3, 4, 3, 'someurl.com', 0)",
              "('remove before flight', 'Jul-9-1995', '', 20, 20, 'great tag!', 3, 4, 3, 'someurl.com', 0)"]
# As SQL will return it
test_item_check = [('remove before flight', 'Jul-9-1995', '', 20, 20, 'great tag!', 3, 4, 3, 'someurl.com', 0),
                    ('remove before flight', 'Jul-9-1995', '', 20, 20, 'great tag!', 3, 4, 3, 'someurl.com', 0)]

# Insert test items into DB
for item in test_items:
    c.execute("INSERT INTO items VALUES {}".format(item))

# Save the changes
conn.commit()
print("Changes committed")

# Print an item from the database to verify it delete them, then verify it's empty
c.execute('SELECT * FROM items')
returns = c.fetchall()

# Test that the Db returns what is expected only asserts on length, could be more strenuous
assert len(returns) == len(test_items)

# Delete the items so the Db is fresh and assert deletion was complete
c.execute('DELETE FROM items')
conn.commit()
assert c.fetchall() == []

# Close connection when done
conn.close()
print("The item-data database is prepared for use")

'''
Create Sales_data Db with following fields:
Post Date               [DATE]
Sold Date               [DATE]
post_price              [INTEGER]
current_price           [INTEGER]
description             [TEXT]
Number of Likes         [INT]
Number of Comments      [INT]
URL to Listing          [STRING/URI]
num_images              [INTEGER]
Refunded (True/False)   [BOOLEAN]
'''
# Create the sales_data.db
conn = sqlite3.connect('../data/sales_data.db')
c = conn.cursor()

# Try to create the db and table, otherwise it already exists
try:
    print("Creating sales_data db...")
    c.execute('''CREATE TABLE sales (item_name TEXT, post_date DATE, sold_date DATE, post_price INTEGER, 
                                    sold_price INTEGER, description TEXT, num_likes INTEGER, num_comments INTEGER, 
                                    num_images INTEGER, url TEXT, refunded INTEGER)''')
    print("DB created")
except OperationalError:
    print(sys.exc_info()[1])

print("Testing Insert...")
# Insert a row of data to test
# As needed for SQL Insert
test_items = ["('remove before flight', 'Jul-9-1995', 'Jul-10-1995', 20, 20, 'great tag!', 3, 4, 3, 'someurl.com', 0)",
              "('remove before flight', 'Jul-9-1995', 'Jul-10-1995', 20, 20, 'great tag!', 3, 4, 3, 'someurl.com', 0)"]
# As SQL will return it
test_item_check = [('remove before flight', 'Jul-9-1995', 'Jul-10-1995', 20, 20, 'great tag!', 3, 4, 3, 'someurl.com', 0),
                    ('remove before flight', 'Jul-9-1995', 'Jul-10-1995', 20, 20, 'great tag!', 3, 4, 3, 'someurl.com', 0)]

# Insert test items into DB
for item in test_items:
    c.execute("INSERT INTO sales VALUES {}".format(item))

# Save the changes
conn.commit()
print("Changes committed")

# Print an item from the database to verify it delete them, then verify it's empty
c.execute('SELECT * FROM sales')
returns = c.fetchall()

# Test that the Db returns what is expected only asserts on length, could be more strenuous
assert len(returns) == len(test_items)

# Delete the items so the Db is fresh and assert deletion was complete
c.execute('DELETE FROM sales')
conn.commit()
assert c.fetchall() == []

# Close connection when done
conn.close()
print("The sales-data database is prepared for use")
