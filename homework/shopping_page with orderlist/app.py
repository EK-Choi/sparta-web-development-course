from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    firstname_receive = request.form['firstname_give']
    lastname_receive = request.form['lastname_give']
    qnts_receive = request.form['qnts_give']
    address_receive = request.form['address_give']
    number_receive = request.form['number_give']

    doc = {
        'first_name': firstname_receive,
        'last_name': lastname_receive,
        'quantities': qnts_receive,
        'address': address_receive,
        'number': number_receive
    }
    db.orderlist.insert_one(doc)

    return jsonify({'msg': 'Your order has been completed!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.orderlist.find({}, {'_id': False}))
    return jsonify({'orderlinfo': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)