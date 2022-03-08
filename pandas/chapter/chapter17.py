"""
이전 과제에서 강의실 크기에 따라 “room assignment” column을 만들어 주었습니다.

이제 이 “room assignment”에 따라 강의실 이름을 붙여주려고 합니다.

아래 세 가지 조건을 만족하도록 코드를 작성하세요.

같은 크기의 강의실이 필요한 과목에 대해 알파벳 순서대로 방 번호를 배정하세요.
예를 들어 Auditorium이 필요한 과목으로 “arts”, “commerce”, “science” 세 과목이 있다면, “arts”는 “Auditorium-1”, “commerce”는 “Auditorium-2”, “science”는 “Auditorium-3” 순서로 방 배정이 되어야 합니다. 방 번호에 room 은 포함되지 않습니다. 아래 스크린샷을 참고하여 작성해주세요.

“status” column이 “not allowed”인 수강생은 “room assignment” column을 그대로 “not assigned”로 남겨둡니다. "not allowed" 인 수강생의 "room assignment" 상태가 변경되지 않도록 유의해주세요.

“room assignment” column의 이름을 “room number”로 바꿔주세요.

"""

import pandas as pd

df = pd.read_csv('data/enrolment_3.csv')

# 코드를 작성하세요.
allowed = df['status'] == 'allowed'

auditorium = df['room assignment'] == 'Auditorium'
large_room = df['room assignment'] == 'Large room'
medium_room = df['room assignment'] == 'Medium room'
small_room = df['room assignment'] == 'Small room'

auditorium_list = list(df.loc[allowed & auditorium, 'course name'].unique())
auditorium_list.sort()
large_room_list = list(df.loc[allowed & large_room, 'course name'].unique())
large_room_list.sort()
medium_room_list = list(df.loc[allowed & medium_room, 'course name'].unique())
medium_room_list.sort()
small_room_list = list(df.loc[allowed & small_room, 'course name'].unique())
small_room_list.sort()

for i in range(len(auditorium_list)):
    df.loc[(df['course name'] == auditorium_list[i]) & allowed, 'room assignment'] = 'Auditorium' + '-' + str(i+1)

for i in range(len(large_room_list)):
    df.loc[(df['course name'] == large_room_list[i]) & allowed, 'room assignment'] = 'Large' + '-' + str(i+1)

for i in range(len(medium_room_list)):
    df.loc[(df['course name'] == medium_room_list[i]) & allowed, 'room assignment'] = 'Medium' + '-' + str(i+1)

for i in range(len(small_room_list)):
    df.loc[(df['course name'] == small_room_list[i]) & allowed, 'room assignment'] = 'Small' + '-' + str(i+1)

df.rename(columns={'room assignment': 'room number'}, inplace=True)
# 정답 출력
print(df.tail(10))