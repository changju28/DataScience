"""
아래와 같은 결과가 나오도록 DataFrame을 만들고 출력해 보세요.
column은 name, birthday, occupation 총 3개입니다.

    name	           birthday	              occupation
0	Taylor Swift	December 13, 1989	   Singer-songwriter
1	Aaron Sorkin	June 9, 1961	       Screenwriter
2	Harry Potter	July 31, 1980	       Wizard
3	Ji-Sung Park	February 25, 1981	   Footballer

"""


import pandas as pd

names = ["Taylor Swift", "Aaron Sorkin", "Harry Potter", "Ji-Sung Park"]
birthdays = ["December 13, 1989", "June 9, 1961", "July 31, 1980", "February 25, 1981"]
occupations = ["Singer-songwriter", "Screenwriter", "Wizard", "Footballer"]

dict = {
    "name": names,
    "birthday": birthdays,
    "occupation": occupations
}

df = pd.DataFrame(dict)

# 정답 출력
print(df)