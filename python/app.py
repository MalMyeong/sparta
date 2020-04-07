from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('meta_prac.html')

@app.route('/memo', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    all_articles = db.memo.find({},{'_id':0})
    articles_list = list(all_articles)
    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success', 'articles':articles_list})

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
    # 1. 클라이언트로부터 데이터를 받기
    comment: str = request.form.get("comment")
    url: str = request.form.get("url")
    # 2. meta tag를 스크래핑하기
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')
     # 3. mongoDB에 데이터 넣기
    doc = {
        'url': url,
        'comment': comment,
        'image': og_image['content'],
        'title': og_title['content'],
        'description': og_description['content']
    }
    result = db.memo.insert_one(doc)
    if result.acknowledged:
        return jsonify({'result': 'success', 'msg':result.inserted_id}) # 어떤 아이디를 통해 결과값이 들어갔는지를 보여주는 것 = inserted_id
    return jsonify({'result':'failed'}) # 실패했을 때

if __name__ == '__main__':
   app.run('localhost',port=5000,debug=True)