import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser') #data.text = 웹사이트에서 우리가 받는 html / parser는 html을 분석해주는 도구(?)
#분석된 html파일이 soup에 들어간 상
movies = soup.select('#old_content > table > tbody > tr') #()안의 내용은 크롬 개발자에서 우클릭 copy>copy selector (개발자 경로)
n = 0
for movie in movies:
    #movie안에 a가 있으면
    a_tag = movie.select_one('td.title > div > a')
    if a_tag is not None:
        n = n + 1
        point = movie.select_one('.point')
        print(n, a_tag.text, point.text)
