
# # 서버 데이터 불러오기
"""
import requests

page = requests.get("https://www.google.com")
print(type(page))

print(page.text)
"""
import requests

""""""
# # 피싱

from bs4 import BeautifulSoup


html_code = """ 
<!DOCTYPE html>
<html>
<head>
    <title>Sample Website</title>
</head>
<body>
<h2>HTML 연습</h2>
<p>
    이것은 첫 번째 문단
</p>
<p>
    이것은 두번째 문단
</p>

<ul>
    <li>커피</li>
    <li>녹차</li>
    <li>우유</li>
</ul>

<img src="https://upload.wikimedia.org/wifipedia/commons/thumb/4/45/A_small_cup_of_coffee.JPG/550px-A_small_cup_of_coffee.JPG">

</body>
</html>
"""

# # BeautifulSoup 사용법
"""
soup = BeautifulSoup(html_code, 'html.parser')

print(type(soup))

li_tags = soup.select('li')

print(li_tags)

print(li_tags[0].text)

butiful_list = []

for i in li_tags:
    butiful_list.append(i.text)

print(butiful_list)

img_tag = soup.select('img')

print(img_tag[0]['src'])
"""
"""
response = requests.get('https://workey.codeit.kr/music/index').text

soup = BeautifulSoup(response, 'html.parser')

# print(soup)

list = soup.select('.popular__order li')

# print(len(list))

popular = []

for i in list:
    a = i.text.replace(' ', '').replace('\n', '')
    popular.append(i.text)

print(popular)

"""
# # 데이터 가져오기
"""
import time
import requests
from bs4 import BeautifulSoup

# 빈 리스트 생성
pages = []

# 첫 페이지 번호 지정
page_num = 1

# headers 지정
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
}

while True:
    # HTML 코드 받아오기, 위에서 지정해 준 headers 설정해 주기
    response = requests.get("http://www.ssg.com/search.ssg?target=all&query=nintendo&page=" + str(page_num), headers=headers)

    # BeautifulSoup 타입으로 변환하기
    soup = BeautifulSoup(response.text, 'html.parser')

    # ".csrch_tip" 클래스가 없을 때만 HTML 코드를 리스트에 담기
    if len(soup.select('.csrch_tip')) == 0:
        pages.append(soup)
        print(str(page_num) + "번째 페이지 가져오기 완료")
        page_num += 1
        time.sleep(3)
    else:
        break

# 가져온 페이지 개수 출력하기
print(len(pages))
"""

# # 가져온데이터 dataframe 만들기
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

# 빈 리스트 생성
records = []

# 시작 페이지 지정
page_num = 1

# headers 지정
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
}

while True:
    # HTML 코드 받아오기
    response = requests.get("http://www.ssg.com/search.ssg?target=all&query=nintendo&page=" + str(page_num),
                            headers=headers)

    # BeautifulSoup 타입으로 변형하기
    soup = BeautifulSoup(response.text, 'html.parser')

    # "prodName" 클래스가 있을 때만 상품 정보 가져오기
    if len(soup.select('.csrch_tip')) == 0:
        product_names = soup.select('.cunit_info > div.cunit_md.notranslate > div > a > em.tx_ko')
        product_prices = soup.select('.cunit_info > div.cunit_price.notranslate > div.opt_price > em')
        product_urls = soup.select('.cunit_prod > div.thmb > a > img')
        page_num += 1
        time.sleep(3)

        # 상품의 정보를 하나의 레코드로 만들고, 리스트에 순서대로 추가하기
        for i in range(len(product_names)):
            record = []
            record.append(product_names[i].text)
            record.append(product_prices[i].text.strip())
            record.append("https://www.ssg.com" + product_urls[i].get('src'))
            records.append(record)
    else:
        break

# 결과 출력
print(len(records))
print(records)

# DataFrame 만들기
df = pd.DataFrame(data = records, columns = ["이름", "가격", "이미지 주소"])

# DataFrame 출력
df.head()