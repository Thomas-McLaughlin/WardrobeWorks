import sqlite3
import sys
from sqlite3 import OperationalError

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

conn = sqlite3.connect('../data/item_data.db')
c = conn.cursor()

try:
    print("Creating item_data db...")
    c.execute('''CREATE TABLE items (item_name TEXT, post_date DATE,
                                     sold_date DATE, post_price INTEGER,
                                     current_price INTEGER, description TEXT,
                                     num_likes INTEGER, num_comments INTEGER,
                                     num_images INTEGER, url TEXT,
                                     refunded INTEGER)''')
    print("DB created")
except OperationalError:
    print(sys.exc_info()[1])

print("Testing Insert...")

test_items = ["('remove before flight', 'Jul-9-1995', '', 20, 20, 'great tag!', 3, 4, 3, 'someurl.com', 0)",
              "('remove before flight', 'Jul-9-1995', '', 20, 20, 'great tag!', 3, 4, 3, 'someurl.com', 0)"]

test_item_check = [('remove before flight', 'Jul-9-1995', '', 20, 20,
                    'great tag!', 3, 4, 3, 'someurl.com', 0),
                   ('remove before flight', 'Jul-9-1995', '', 20, 20,
                    'great tag!', 3, 4, 3, 'someurl.com', 0)]

for item in test_items:
    c.execute("INSERT INTO items VALUES {}".format(item))

conn.commit()
print("Changes committed")

c.execute('SELECT * FROM items')
returns = c.fetchall()

assert len(returns) == len(test_items)

c.execute('DELETE FROM items')
conn.commit()
assert c.fetchall() == []

conn.close()
print("The item-data database is prepared for use")

'''
Create sales_data db with following fields:
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

conn = sqlite3.connect('../data/sales_data.db')
c = conn.cursor()

try:
    print("Creating sales_data db...")
    c.execute('''CREATE TABLE sales (item_name TEXT, post_date DATE,
                                     sold_date DATE, post_price INTEGER,
                                    sold_price INTEGER, description TEXT,
                                    num_likes INTEGER, num_comments INTEGER,
                                    num_images INTEGER, url TEXT,
                                    refunded INTEGER)''')
    print("DB created")
except OperationalError:
    print(sys.exc_info()[1])

print("Testing Insert...")

test_items = ["('remove before flight', 'Jul-9-1995', 'Jul-10-1995', 20, 20, 'great tag!', 3, 4, 3, 'someurl.com', 0)",
              "('remove before flight', 'Jul-9-1995', 'Jul-10-1995', 20, 20, 'great tag!', 3, 4, 3, 'someurl.com', 0)"]

test_item_check = [('remove before flight', 'Jul-9-1995', 'Jul-10-1995',
                    20, 20, 'great tag!', 3, 4, 3, 'someurl.com', 0),
                   ('remove before flight', 'Jul-9-1995', 'Jul-10-1995',
                    20, 20, 'great tag!', 3, 4, 3, 'someurl.com', 0)]

for item in test_items:
    c.execute("INSERT INTO sales VALUES {}".format(item))

conn.commit()
print("Changes committed")

c.execute('SELECT * FROM sales')
returns = c.fetchall()

assert len(returns) == len(test_items)

c.execute('DELETE FROM sales')
conn.commit()
assert c.fetchall() == []

conn.close()
print("The sales-data database is prepared for use")
