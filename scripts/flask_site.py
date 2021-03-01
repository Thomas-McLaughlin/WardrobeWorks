from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import sys
from sqlite3 import OperationalError
from werkzeug.exceptions import BadRequest

app = Flask(__name__)


@app.route('/')
def index():
    """Renders the index page template."""
    return render_template('index.html')


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
    if request.method == 'POST':

        try:
            itemName = request.form['itemName']
        except BadRequest:
            itemName = '-'

        try:
            itemPrice = request.form['itemPrice']
        except BadRequest:
            itemPrice = 0

        try:
            current_price = itemPrice
        except BadRequest:
            current_price = 0

        try:
            costOfGoods = request.form['costOfGoods']
        except BadRequest:
            costOfGoods = 0

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

        post_date = '-'
        sell_date = '-'

        likes = 0
        comments = 0
        num_pictures = 0
        url = '-'  # If it is '-', then it is not listed

        try:
            conn = sqlite3.connect('../data/item_data.db')
            c = conn.cursor()
        except OperationalError:
            print(sys.exc_info()[1])

        item = (itemName, post_date, sell_date, itemPrice, current_price,
                costOfGoods, designer, size, condition,
                description, likes, comments, num_pictures, url, 0)

        command = "insert into items (item_name, post_date, sold_date, " \
                  "post_price, current_price, cost_of_goods, designer, " \
                  "size, condition, description, num_likes, num_comments, " \
                  "num_images, url, refunded) values {}".format(item)

        c.execute(command)
        conn.commit()
        conn.close()

        return redirect(url_for('post'))
    else:
        redirect(url_for('index'))


@app.route('/sales')
def sales():
    return render_template('sales.html')
