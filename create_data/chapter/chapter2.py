import requests

# 코드를 작성하세요
rating_pages = []

for i in range(2010, 2013):
    for j in range(1, 13):
        for w in range(0, 4):
            page = "https://workey.codeit.kr/ratings/index?year={0}&month={1}&weekIndex={2}".format(i, j, w)
            domain = requests.get(page).text
            rating_pages.append(domain)


# 테스트 코드
print(len(rating_pages)) # 가져온 총 페이지 수
print(rating_pages[0]) # 첫 번째 페이지의 HTML 코드