import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#유저 정보를 입력함으로써 크롤링 시도가 막히는 것을 방지
data = requests.get('https://www.genie.co.kr/chart/top200',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr > td.info')
n = 0

for music in musics:
    n = n+1
    title = music.find('a', {'class':'title ellipsis'})
    a_title = title.text.strip()
    artist = music.find('a', {'class':'artist ellipsis'})
    a_artist = artist.text
    album = music.find('a', {'class':'albumtitle ellipsis'})
    a_album = album.text
    print(n, a_title, a_artist, a_album)