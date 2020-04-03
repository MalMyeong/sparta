from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

@app.route('/')
def home():
    return render_template('4week.html')

@app.route('/order', methods=['POST'])
def write_order():
    name = request.form['name']
    address = request.form['address']
    phone = request.form['phone']
    color = request.form['color']
    doc = {
        'name': name,
        'color': color,
        'address': address,
        'phone': phone
    }
    db.order.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '주문이 성공적으로 접수되었습니다.'} )

@app.route('/order', methods=['GET'])
def read_order():
    order = list(db.order.find({},{'_id':0}))
    return jsonify({'result': 'success', 'order': order})

if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)