from flask import Flask, render_template
app = Flask(__name__)
# 플라스크 앱을 실행할 대상? 이 __name__, 그걸 플라스크에 알려주면 거기서 플라스크를 실행할 수 있다.

 # 0.0.0.0:5000/ 라는 기본 주소
@app.route('/') # 앱의 기본 경로에 접속했을 때 어떤 함수를 실행할 것이냐 '/'의 의미
def home():
    return render_template('index.html')
@app.route('/yourpage')
def yourpage():
    return 'This is Your Page'
@app.route('/movies')
def movies():
    return 'This is movies!'

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

# flask 해당 주소로 접속했을 때 무엇이 실행될 지 설정하는 것