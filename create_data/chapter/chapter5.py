import requests
from bs4 import BeautifulSoup

# 코드를 작성하세요.
years = range(2010, 2013)
months = range(1, 13)
weekIndexs = range(0, 5)
rating_pages = []
for year in years:
    for month in months:
        for weekIndex in weekIndexs:
            url = "https://workey.codeit.kr/ratings/index?year={0}&month={1}&weekIndex={2}".format(year, month, weekIndex)
            response = requests.get(url).text
            soup = BeautifulSoup(response, 'html.parser')
            if len(soup.select('.row')) < 2:
                break
            else:
                rating_pages.append(response)


# 테스트 코드
print(len(rating_pages)) # 가져온 총 페이지 수
print(rating_pages[1]) # 첫 번째 페이지의 HTML 코드