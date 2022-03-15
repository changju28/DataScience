import pandas as pd
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
            url = "https://workey.codeit.kr/ratings/index?year={0}&month={1}&weekIndex={2}".format(2010, 1, weekIndex)
            response = requests.get(url).text
            soup = BeautifulSoup(response, 'html.parser')
            if len(soup.select('.row')) > 1:
                period = soup.select('option[selected=selected]')[2].text
                rank = soup.select('.row .rank')
                channel = soup.select('.row .channel')
                program = soup.select('.row .program')
                rating = soup.select('.row .percent')
                for i in range(1, len(rank)):
                    channel_ranking = []
                    channel_ranking.append(period)
                    channel_ranking.append(rank[i].text)
                    channel_ranking.append(channel[i].text)
                    channel_ranking.append(program[i].text)
                    channel_ranking.append(rating[i].text)
                    rating_pages.append(channel_ranking)

# 결과 출력
df = pd.DataFrame(data=rating_pages, columns=['period', 'rank', 'channel', 'program', 'rating'])

print(df.head())