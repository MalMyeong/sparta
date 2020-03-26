import requests
from bs4 import BeautifulSoup

URL = 'https://www.genie.co.kr/chart/top200'
request = requests.get(URL)
soup = BeautifulSoup(request.text, 'html.parser')

music = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

print(music)