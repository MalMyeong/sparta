import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#유저 정보를 입력함으로써 크롤링 시도가 막히는 것을 방지
data = requests.get('https://www.genie.co.kr/chart/top200',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr > td.info')
rank = 1

for music in musics:
    title = music.find('a', {'class':'title ellipsis'})
    a_title = title.text.strip()
    artist = music.find('a', {'class':'artist ellipsis'})
    a_artist = artist.text
    album = music.find('a', {'class':'albumtitle ellipsis'})
    a_album = album.text
    print(rank, a_title, a_artist, a_album)
    doc = {
        'rank': rank,
        'title': a_title,
        'artist': a_artist,
        'album': a_album
    }
    db.musics.insert_one(doc)
    rank += 1