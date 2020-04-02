from flask import Flask, render_template, jsonify, request #표준이 JSON이기 때문에 jsonify를 사용한다.(jsonify를 사용하면 그 결과는 JSON이다.)
app = Flask(__name__)

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html') #html 형태로 리턴을 보내고 싶다.

## API 역할을 하는 부분
@app.route('/test', methods=['POST']) # post, get 각자의 역할 하도록 함수 정의해야한다.
def test_post(): # 지정한 함수에 따라 작동
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'}) # json 형태로 리턴을 보내고 싶다.

@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   # localhost:5000/test?title_give=this_is_sparta 했을 때 argument는 title_give(key)라는 값을 받고 그 결과가 this_is_sparta(value)이고, msg 값에 넣어준다.
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

if __name__ == '__main__':
   app.run('localhost',port=5000,debug=True)
   #주소 ->localhost:5000 (이전까지 ' '안의 값이 0.0.0.0이었기 때문에 test에 대한 주소가 정의 되지 않아 get,post가 되지 않았었다.)
   # body -> form-data 이유는 위의 test_post에서 title_receive는 form을 받기 때문이다.