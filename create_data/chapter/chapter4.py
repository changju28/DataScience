import requests
from bs4 import BeautifulSoup

# 코드를 작성하세요

response = requests.get('https://workey.codeit.kr/music/index').text

soup = BeautifulSoup(response, 'html.parser')

popular_artist = soup.select('.rank__order .list')

search_ranks = []

for artist in popular_artist:
    slicing = artist.text[5:]
    artist = slicing.replace('\n', '').strip()
    search_ranks.append(artist)


# 결과 출력
print(search_ranks)