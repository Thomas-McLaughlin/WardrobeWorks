# import things
from flask_table import Table, Col

'''
Item fields:
item_name               [TEXT]            : The name of the item
post_date               [DATE]            : The date the item was posted
sold_date               [DATE]            : The date the item was sold
post_price              [INTEGER]         : The price the item was posted with
current_price           [INTEGER]         : The current price of the item, if listing is active
cost_of_goods           [INTEGER]         : Optional, what the user paid for the item (used for profit calc)
sold_price              [INTEGER]         : The price that the item sold for
description             [TEXT]            : The description the item was posted with
designer                [TEXT]            : The designer of the item
category                [INTEGER]         : The category the item was posted in
size                    [INTEGER]         : The size of the item
condition               [TEXT]            : The condition of the item
num_bumps               [INTEGER]         : The number of times the item has been bumped
num_likes               [INTEGER]         : The number of times the item was liked
num_comments            [INTEGER]         : The number of comments on the item
num_images              [INTEGER]         : The number of images used in the listing
URL                     [STRING/URI]      : The URL to the listing
Refunded (True/False)   [INTEGER]         : Was a refund requested on the item?
rating                  [INTEGER]         : What did the customer rate the transaction?
sale_to_delivery        [INTEGER]         : How long did it take for the customer to get the item after sale?
'''


# Declare your table
class SalesTable(Table):
    item_name = Col('Name')
    post_date = Col('Posted')
    sold_date = Col('Sold')
    post_price = Col('Posted At')
    current_price = Col('Current Price')
    cost_of_goods = Col('Cost of Goods')
    sold_price = Col('Sold For')
    description = Col('Description')
    designer = Col('Designer')
    category = Col('Category')
    size = Col('size')
    condition = Col('Condition')
    num_bumps = Col('Bumps')
    num_likes = Col('Likes')
    num_comments = Col('Comments')
    num_images = Col('Images')
    url = Col('Link')
    refunded = Col('Refunded')
    rating = Col('Rating')
    sale_to_delivery = Col('Time to Delivery')


# Get some objects
class Sale(object):
    def __init__(self, item_name, post_date, sold_date, post_price, current_price, cost_of_goods, sold_price,
                 description, designer, category, size, condition, num_bumps, num_likes, num_comments,
                 num_images, url, refunded, rating, sale_to_delivery):
        self.item_name = item_name
        self.post_date = post_date
        self.sold_date = sold_date
        self.post_price = post_price
        self.current_price = current_price
        self.cost_of_goods = cost_of_goods
        self.sold_price = sold_price
        self.description = description
        self.designer = designer
        self.category = category
        self.size = size
        self.condition = condition
        self.num_bumps = num_bumps
        self.num_likes = num_likes
        self.num_comments = num_comments
        self.num_images = num_images
        self.url = url
        self.refunded = refunded
        self.rating = rating
        self.sale_to_delivery = sale_to_delivery


'''
Item fields:
item_name               [TEXT]            : The name of the item
post_date               [DATE]            : The date the item was posted
sold_date               [DATE]            : The date the item was sold
post_price              [INTEGER]         : The price the item was posted with
current_price           [INTEGER]         : The current price of the item, if listing is active
cost_of_goods           [INTEGER]         : Optional, what the user paid for the item (used for profit calc)
description             [TEXT]            : The description the item was posted with
designer                [TEXT]            : The designer of the item
category                [INTEGER]         : The category the item was posted in
size                    [INTEGER]         : The size of the item
condition               [TEXT]            : The condition of the item
num_bumps               [INTEGER]         : The number of times the item has been bumped
num_likes               [INTEGER]         : The number of times the item was liked
num_comments            [INTEGER]         : The number of comments on the item
num_images              [INTEGER]         : The number of images used in the listing
URL                     [STRING/URI]      : The URL to the listing
Refunded (True/False)   [INTEGER]         : Was a refund requested on the item?
rating                  [INTEGER]         : What did the customer rate the transaction?
sale_to_delivery        [INTEGER]         : How long did it take for the customer to get the item after sale?
'''


# Declare your table
class ItemTable(Table):
    item_name = Col('Name')
    post_date = Col('Posted')
    sold_date = Col('Sold')
    post_price = Col('Posted At')
    current_price = Col('Current Price')
    cost_of_goods = Col('Cost of Goods')
    description = Col('Description')
    designer = Col('Designer')
    category = Col('Category')
    size = Col('size')
    condition = Col('Condition')
    num_bumps = Col('Bumps')
    num_likes = Col('Likes')
    num_comments = Col('Comments')
    num_images = Col('Images')
    url = Col('Link')


# Get some objects
class Item(object):
    def __init__(self, item_name, post_date, sold_date, post_price, current_price, cost_of_goods,
                 description, designer, category, size, condition, num_bumps, num_likes, num_comments,
                 num_images, url):
        self.item_name = item_name
        self.post_date = post_date
        self.sold_date = sold_date
        self.post_price = post_price
        self.current_price = current_price
        self.cost_of_goods = cost_of_goods
        self.description = description
        self.designer = designer
        self.category = category
        self.size = size
        self.condition = condition
        self.num_bumps = num_bumps
        self.num_likes = num_likes
        self.num_comments = num_comments
        self.num_images = num_images
        self.url = url
