import sqlite3
import sys
from sqlite3 import OperationalError

'''
Create item_data db with following fields:
item_name               [TEXT]            : The name of the item
post_date               [DATE]            : The date the item was posted
sold_date               [DATE]            : The date the item was sold
post_price              [INTEGER]         : The price the item was posted with
current_price           [INTEGER]         : The current price of the item, if listing is active
cost_of_goods           [INTEGER]         : Optional, what the user paid for the item (used for profit calc)
sold_price              [INTEGER]         : The price that the item sold for
description             [TEXT]            : The description the item was posted with
designer                [TEXT]            : The designer of the item
category                [INT]             : The category the item was posted in
size                    [INT]             : The size of the item
condition               [TEXT]            : The condition of the item
num_bumps               [INT]             : The number of times the item has been bumped
num_likes               [INT]             : The number of times the item was liked
num_comments            [INT]             : The number of comments on the item
num_images              [INTEGER]         : The number of images used in the listing
URL                     [STRING/URI]      : The URL to the listing
'''

# Open a connection to the database
conn = sqlite3.connect('../data/item_data.db')
c = conn.cursor()

# Create the item_data db if it doesn't exist yet
try:
    print("Creating item_data db...")
    c.execute('''CREATE TABLE items
                    (item_name TEXT,
                    post_date DATE,
                    sold_date DATE,
                    post_price INTEGER,
                    current_price INTEGER,
                    cost_of_goods INTEGER,
                    description TEXT,
                    designer TEXT,
                    category INTEGER,
                    size INTEGER,
                    condition TEXT,
                    num_bumps INTEGER,
                    num_likes INTEGER,
                    num_comments INTEGER,
                    num_images INTEGER,
                    url TEXT)''')
    print("item_data DB created")
except OperationalError:
    print(sys.exc_info()[1])

# Test the database
print("Testing Insert...")
test_items = ["('remove before flight', '', '', 20, 20, 5, 'great tag!', 'None', 0, 0, 'New', 0, 0, 0, 3, 'someurl.com')",
              "('remove before flight', '', '', 20, 20, 5, 'great tag!', 'None', 0, 0, 'New', 0, 0, 0, 3, 'someurl.com')"]

test_item_check = [('remove before flight', '', '', 20, 20, 5, 'great tag!', 'None', 0, 0, 'New', 0, 0, 0, 3, 'someurl.com'),
                   ('remove before flight', '', '', 20, 20, 5, 'great tag!', 'None', 0, 0, 'New', 0, 0, 0, 3, 'someurl.com')]

for item in test_items:
    c.execute("INSERT INTO items VALUES {}".format(item))
conn.commit()
print("Changes committed")
c.execute('SELECT * FROM items')
returns = c.fetchall()
assert len(returns) == len(test_items)

# # Clear the test from the db
# c.execute('DELETE FROM items')
# conn.commit()
# assert c.fetchall() == []

# Close the connection and notify user
conn.close()
print("The item-data database is prepared for use")

'''
Create sales_data db with following fields:
item_name               [TEXT]            : The name of the item
post_date               [DATE]            : The date the item was posted
sold_date               [DATE]            : The date the item was sold
post_price              [INTEGER]         : The price the item was posted with
current_price           [INTEGER]         : The current price of the item, if listing is active
cost_of_goods           [INTEGER]         : Optional, what the user paid for the item (used for profit calc)
sold_price              [INTEGER]         : The price that the item sold for
description             [TEXT]            : The description the item was posted with
designer                [TEXT]            : The designer of the item
category                [INTEGER]             : The category the item was posted in
size                    [INTEGER]             : The size of the item
condition               [TEXT]            : The condition of the item
num_bumps               [INTEGER]             : The number of times the item has been bumped
num_likes               [INTEGER]             : The number of times the item was liked
num_comments            [INTEGER]             : The number of comments on the item
num_images              [INTEGER]         : The number of images used in the listing
URL                     [STRING/URI]      : The URL to the listing
Refunded (True/False)   [INTEGER]             : Was a refund requested on the item?
rating                  [INTEGER]             : What did the customer rate the transaction?
sale_to_delivery        [INTEGER]             : How long did it take for the customer to get the item after sale?
'''

# Open a connection to the database
conn = sqlite3.connect('../data/sales_data.db')
c = conn.cursor()

# Create the sales_data db if it doesn't exist yet
try:
    print("Creating sales_data db...")
    c.execute('''CREATE TABLE sales
                    (item_name TEXT,
                    post_date DATE,
                    sold_date DATE,
                    post_price INTEGER,
                    current_price INTEGER,
                    cost_of_goods INTEGER,
                    sold_price INTEGER,
                    description TEXT,
                    designer TEXT,
                    category INTEGER,
                    size INTEGER,
                    condition TEXT,
                    num_bumps INTEGER,
                    num_likes INTEGER,
                    num_comments INTEGER,
                    num_images INTEGER,
                    url TEXT,
                    refunded INTEGER,
                    rating INTEGER,
                    sale_to_delivery INTEGER)''')
    print("sales_data DB created")
except OperationalError:
    print(sys.exc_info()[1])

# Test the database
print("Testing Insert...")
test_items = ["('remove before flight', 'Jul-9-1995', 'Jul-10-1995', 20, 20, 5, 20, 'great tag!', 'None', 0, 0, 'New', 0, 0, 0, 3, 'someurl.com', 0, 5, 3)",
              "('remove before flight', 'Jul-9-1995', 'Jul-10-1995', 20, 20, 5, 20, 'great tag!', 'None', 0, 0, 'New', 0, 0, 0, 3, 'someurl.com', 0, 5, 3)"]

test_item_check = [('remove before flight', 'Jul-9-1995', 'Jul-10-1995', 20, 20, 5, 20, 'great tag!', 'None', 0, 0, 'New', 0, 0, 0, 3, 'someurl.com', 0, 5, 3),
                   ('remove before flight', 'Jul-9-1995', 'Jul-10-1995', 20, 20, 5, 20, 'great tag!', 'None', 0, 0, 'New', 0, 0, 0, 3, 'someurl.com', 0, 5, 3)]


for item in test_items:
    c.execute("INSERT INTO sales VALUES {}".format(item))
conn.commit()
print("Changes committed")
c.execute('SELECT * FROM sales')
returns = c.fetchall()
assert len(returns) == len(test_items)

# # Clear the test from the db
# c.execute('DELETE FROM sales')
# conn.commit()
# assert c.fetchall() == []

# Close the connection and notify user
conn.close()
print("The sales-data database is prepared for use")
