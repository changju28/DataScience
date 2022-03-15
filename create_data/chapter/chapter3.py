import requests
from bs4 import BeautifulSoup

# 코드를 작성하세요

response = requests.get('https://workey.codeit.kr/orangebottle/index').text

soup = BeautifulSoup(response, 'html.parser')

phone_number = soup.select('.container .branch .phoneNum')

phone_numbers = []

for number in phone_number:
    phone_numbers.append(number.text)




# 결과 출력
print(phone_numbers)