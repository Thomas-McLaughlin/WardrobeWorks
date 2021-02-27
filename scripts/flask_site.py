from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post')
def post():
    return render_template('post.html')


@app.route('/post', methods=['POST', 'GET'])
def my_form_post():
    if request.method == 'POST':
        itemName = request.form['itemName']
        itemprice = request.form['itemPrice']
        costOfGoods = request.form['costOfGoods']
        description = request.form['description']
        designer = request.form['designer']
        size = request.form['size']
        condition = request.form['condition']
        print(itemName, itemprice, costOfGoods, description, designer, size, condition)
        return redirect(url_for('post'))
    else:
        redirect(url_for('index'))


@app.route('/sales')
def sales():
    return render_template('sales.html')
