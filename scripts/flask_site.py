from flask import Flask, render_template, request, redirect, url_for, Markup
import sqlite3
import sys
import os
from sqlite3 import OperationalError
from werkzeug.exceptions import BadRequest
import json
from json2html import *

app = Flask(__name__)


@app.route('/')
def index():
    """Renders the index page template."""
    try:
        conn = sqlite3.connect('../data/item_data.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
    except OperationalError:
        print(sys.exc_info()[1])
    c.execute('SELECT * FROM items')
    rows = c.fetchall()
    data = json.dumps([dict(ix) for ix in rows])  # CREATE JSON
    conn.close()
    return render_template('manage.html', table=Markup(json2html.convert(json=data, table_attributes="class=\"table table-sm\"")))


@app.route('/post')
def post():
    """
    Renders the post page template.

    The post page is the interface by which users can add
    new items to their database. Users can then select items to
    post from their manage page.

    Returns:
        post.html
    """
    return render_template('post.html')


@app.route('/post', methods=['POST', 'GET'])
def my_form_post():
    """
    Form for capturing and writing new items to the user's database
    """
    '''
    Item fields:
    x item_name               [TEXT]            : The name of the item
    x post_date               [DATE]            : The date the item was posted
    x sold_date               [DATE]            : The date the item was sold
    x post_price              [INTEGER]         : The price the item was posted with
    x current_price           [INTEGER]         : The current price of the item, if listing is active
    x cost_of_goods           [INTEGER]         : Optional, what the user paid for the item (used for profit calc)
    x sold_price              [INTEGER]         : The price that the item sold for
    x description             [TEXT]            : The description the item was posted with
    x designer                [TEXT]            : The designer of the item
    x category                [INTEGER]         : The category the item was posted in
    x size                    [INTEGER]         : The size of the item
    x condition               [TEXT]            : The condition of the item
    x num_bumps               [INTEGER]         : The number of times the item has been bumped
    x num_likes               [INTEGER]         : The number of times the item was liked
    x num_comments            [INTEGER]         : The number of comments on the item
    x num_images              [INTEGER]         : The number of images used in the listing
    x URL                     [STRING/URI]      : The URL to the listing
    x Refunded (True/False)   [INTEGER]         : Was a refund requested on the item?
    x rating                  [INTEGER]         : What did the customer rate the transaction?
    x sale_to_delivery        [INTEGER]         : How long did it take for the customer to get the item after sale?
    '''

    if request.method == 'POST':
        # Gather data from form
        try:
            item_name = request.form['itemName']
        except BadRequest:
            item_name = '-'

        try:
            post_price = request.form['itemPrice']
        except BadRequest:
            post_price = 0

        try:
            current_price = post_price
        except BadRequest:
            current_price = 0

        try:
            cost_of_goods = request.form['costOfGoods']
        except BadRequest:
            cost_of_goods = 0

        try:
            description = request.form['description']
        except BadRequest:
            description = '-'

        try:
            designer = request.form['designer']
        except BadRequest:
            designer = 0

        try:
            size = request.form['size']
        except BadRequest:
            size = '-'

        try:
            condition = request.form['condition']
        except BadRequest:
            condition = 0

        try:
            category = request.form['category']
        except BadRequest:
            category = 'None'

        # Set placeholders for values under manage view's responsibility
        post_date = '-'
        sold_date = '-'
        sold_price = 0
        likes = 0
        bumps = 0
        comments = 0
        num_pictures = 0
        url = '-'  # If it is '-', then it is not listed

        try:
            conn = sqlite3.connect('../data/item_data.db')
            c = conn.cursor()
        except OperationalError:
            print(sys.exc_info()[1])

        item = (item_name, post_date, sold_date, post_price, current_price,
                cost_of_goods, description, designer, category, size, condition,
                bumps, likes, comments, num_pictures, url)

        command = "insert into items (item_name, post_date, sold_date," \
                  "post_price, current_price, cost_of_goods, description, designer, " \
                  "category, size, condition, num_bumps, num_likes, num_comments, " \
                  "num_images, url) values {}".format(item)
        c.execute(command)
        conn.commit()
        conn.close()

        return redirect(url_for('post'))
    else:
        redirect(url_for('index'))


@app.route('/sales')
def sales():
    try:
        conn = sqlite3.connect('../data/sales_data.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
    except OperationalError:
        print(sys.exc_info()[1])
    c.execute('SELECT * FROM sales')
    rows = c.fetchall()
    data = json.dumps([dict(ix) for ix in rows])  # CREATE JSON
    conn.close()
    return render_template('sales.html', table=Markup(json2html.convert(json=data, table_attributes="class=\"table table-responsive-sm\"")))
